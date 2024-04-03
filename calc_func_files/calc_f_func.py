# -*- coding: utf-8 -*-
# @Time        : 2024/3/25 13:38
# @Author      : husky
# @FileName    : calc_f_func.py
# @Software    : PyCharm
# @ProjectName : ICSS-Slope
# @Email       : shiguihuang1874@qq.com
import numpy as np
import pandas as pd

"""
输入的参数为：
坡高： H

黏聚力：c
重度： gamma
内摩擦角：varphi

地下水系数：r_u
水平地震系数：alpha_w
"""


# 先定义一个函数，根据 r_u 和 alpha_w 获取需要的 f_x 和 f_y
def get_f_x_y(r_u_: float, alpha_w_: float) -> list:
    """
    根据 r_u 和 alpha_w 判断需要的 f_x 和 f_y
    :param r_u_: float, 地下水影响因子
    :param alpha_w_: float, 水平地震影响因子
    :return:
            judge_sheet_name: list, 返回需要读取的Excel Sheet名
    """
    data_read = ".\\para_files\\f_calc_paras.xlsx"

    # 判断需要的Sheet名
    if r_u_ == 0 and alpha_w_ == 0:
        judge_sheet_name = ["r_u=0, alpha_w=0"]
    elif alpha_w_ == 0:
        if 0 <= r_u_ <= 0.25:
            judge_sheet_name = ["r_u=0, alpha_w=0", "r_u=0.25"]
        elif 0.25 < r_u_ <= 0.50:
            judge_sheet_name = ["r_u=0.25", "r_u=0.50"]
        else:
            raise ValueError(
                "Groundwater impact factor or horizontal earthquake impact factor error, please check!\n地下水影响因子或水平地震影响因子错误，请检查！")
    elif r_u_ == 0:
        if 0 <= alpha_w_ <= 0.05:
            judge_sheet_name = ["r_u=0, alpha_w=0", "alpha_w=0.05"]
        elif 0.05 < alpha_w_ <= 0.10:
            judge_sheet_name = ["alpha_w=0.05", "alpha_w=0.10"]
        else:
            raise ValueError(
                "Groundwater impact factor or horizontal earthquake impact factor error, please check!\n地下水影响因子或水平地震影响因子错误，请检查！")
    else:
        raise ValueError(
            "Groundwater impact factor or horizontal earthquake impact factor error, please check!\n地下水影响因子或水平地震影响因子错误，请检查！")

    # 根据判断得到Sheet名读取相应的f_x, f_y
    if len(judge_sheet_name) == 1:
        data = pd.read_excel(data_read, sheet_name=judge_sheet_name[0])
        f_x = np.array(data.iloc[:, 0])
        f_y = np.array(data.iloc[:, 1])
        return [[f_x], [f_y]]
    else:
        data_1 = pd.read_excel(data_read, sheet_name=judge_sheet_name[0])
        data_2 = pd.read_excel(data_read, sheet_name=judge_sheet_name[1])
        f_x_1 = np.array(data_1.iloc[:, 0])
        f_y_1 = np.array(data_1.iloc[:, 1])
        f_x_2 = np.array(data_2.iloc[:, 0])
        f_y_2 = np.array(data_2.iloc[:, 1])
        return [[f_x_1, f_x_2], [f_y_1, f_y_2]]


# 使用一组f_x, f_y 计算 f_
def get_f(f_x_, f_y_, x_c_, y_c_):
    # 定义一个内部函数，用于计算直线方程
    def get_lines(x_, y_):
        """
        计算直线方程
        :param x_: 数组类型的x值
        :param y_: 数组值类型的y值
        :return:
               k_: 数组类型的k值
               b_: 数组类型的b值
        """
        x_i = x_[:-1]
        x_i_1 = x_[1:]
        y_i = y_[:-1]
        y_i_1 = y_[1:]
        k_ = (y_i - y_i_1) / (x_i - x_i_1)
        b_ = y_i - k_ * x_i
        return k_, b_

    # 1. 计算直线方程
    # 1.1 计算当前直线方程
    k_c = y_c_ / x_c_
    b_c = 0
    # 1.2 计算直线组参数
    k_i, b_i = get_lines(f_x_, f_y_)

    # 2. 分别计算交点
    x_ji = (b_i - b_c) / (k_c - k_i)
    y_ji = k_c * x_ji

    # 3. 判断交点
    x_j, y_j = 0, 0
    for i in range(len(x_ji)):
        # print(i, x_line_array[i], x_ji[i], x_line_array[i+1], "\t\t", y_ji[i])
        if f_x_[i] <= x_ji[i] <= f_x_[i + 1]:
            # print("intersection point is ({:.4f}, {:.4f})".format(x_ji[i], y_ji[i]))
            x_j, y_j = x_ji[i], y_ji[i]
            # break

    # 4. 计算安全系数f
    f_c_ = y_c_ / y_j
    # print("(x_j:{:.3f}, y_j:{:.3f}), (x_c:{:.3f}, y_c:{:.3f})".format(x_j, y_j, x_c_, y_c_))
    # print("f is {:.4f}".format(f_))
    return f_c_


# 使用得到的 f_x, f_y 计算 f
def get_f_mean(f_x_, f_y_, x_c_, y_c_, r_u_, alpha_w_):
    # print(f_x_)
    if len(f_x_) == 1:
        # pass
        f_mean_ = get_f(f_x_[0], f_y_[0], x_c_, y_c_)
        # print(f_mean_)
    else:
        f_mean_1 = get_f(f_x_[0], f_y_[0], x_c_, y_c_)
        f_mean_2 = get_f(f_x_[1], f_y_[1], x_c_, y_c_)
        if alpha_w_ == 0:
            if r_u_ <= 0.25:
                f_mean_ = (r_u_ - 0.0) * (f_mean_2 - f_mean_1) / (0.25 - 0.0) + f_mean_1
            else:
                f_mean_ = (r_u_ - 0.25) * (f_mean_2 - f_mean_1) / (0.50 - 0.25) + f_mean_1
        else:
            if alpha_w_ <= 0.05:
                f_mean_ = (alpha_w_ - 0.0) * (f_mean_2 - f_mean_1) / (0.05 - 0.0) + f_mean_1
            else:
                f_mean_ = (alpha_w_ - 0.05) * (f_mean_2 - f_mean_1) / (0.10 - 0.05) + f_mean_1
    return f_mean_


# 定义一个获取f函数
def get_f_(r_u_, alpha_w_, c_, gamma_, varphi_):
    varphi_rad_ = np.radians(varphi_)
    x_c_ = c_ / (gamma_ * 25)
    y_c_ = np.tan(varphi_rad_)

    f_x_, f_y_ = get_f_x_y(r_u_, alpha_w_)
    f_mean_ = get_f_mean(f_x_, f_y_, x_c_, y_c_, r_u_, alpha_w_)
    return f_mean_


if __name__ == "__main__":
    # r_u = 0
    # alpha_w = 0
    #
    # c = 28.9
    # gamma = 19.6
    # H = 25
    # varphi = 12.5
    # beta = 30

    H, beta, c, varphi, gamma, r_u, alpha_w = 25, 30, 28.9, 12.5, 19.6, 0, 0

    f_ = get_f_(r_u, alpha_w, c, gamma, varphi)

    print(f_)
