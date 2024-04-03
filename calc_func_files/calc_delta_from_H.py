# -*- coding: utf-8 -*-
# @Time        : 2024/3/27 9:41
# @Author      : husky
# @FileName    : calc_delta_from_H.py
# @Software    : PyCharm
# @ProjectName : ICSS-Slope
# @Email       : shiguihuang1874@qq.com

"""
该文件中的函数实现的功能为从指定(即是无需经过插值法)的 alpha_w, r_u, H_star 函数中计算与 H (需要经过插值法)相关的 delta
"""
import numpy as np
import pandas as pd


# 定义一个函数，根据参数确定要打开的Excel文件及Sheet名
def get_file_and_sheet_name(alpha_w_, r_u_, H_star_):
    # 判断需要的文件名
    if r_u_ == 0 and alpha_w_ == 0:
        file_name_ = ".\\para_files\\r_u=0,alpha_w=0.xlsx"
    elif r_u_ == 0 and alpha_w_ == 0.05:
        file_name_ = ".\\para_files\\alpha_w=0.05.xlsx"
    elif r_u_ == 0 and alpha_w_ == 0.10:
        file_name_ = ".\\para_files\\alpha_w=0.10.xlsx"
    elif r_u_ == 0.25 and alpha_w_ == 0:
        file_name_ = ".\\para_files\\r_u=0.25.xlsx"
    elif r_u_ == 0.50 and alpha_w_ == 0:
        file_name_ = ".\\para_files\\r_u=0.50.xlsx"
    else:
        raise ValueError(
            "Parameters error passed in \"get_file_and_sheet_name\" function!\n\"get_file_and_sheet_name\"函数传入的参数错误！")

    # 判断需要的Sheet名
    if H_star_ == 0.25:
        sheet_name_ = "H_star=0.25"
    elif H_star_ == 1:
        sheet_name_ = "H_star=1"
    elif H_star_ == 3:
        sheet_name_ = "H_star=3"
    elif H_star_ == 5:
        sheet_name_ = "H_star=5"
    elif H_star_ == 15:
        sheet_name_ = "H_star=15"
    elif H_star_ == 35:
        sheet_name_ = "H_star=35"
    elif H_star_ == 45:
        sheet_name_ = "H_star=45"
    else:
        raise ValueError(
            "Parameters error passed in \"get_file_and_sheet_name\" function!\n\"get_file_and_sheet_name\"函数传入的参数错误！")
    return file_name_, sheet_name_


# 定义一个函数，根据H的确定要读取的列，以及获取前后的H值
def get_iloc_of_beta(H_):
    # 定义iloc_of_beta_和H_current
    H_current_ = [None, None]
    iloc_of_beta_ = [None, None]
    if 10 <= H_ < 40:
        iloc_of_beta_[0] = int((H_ - 10) / 5) * 3
        H_current_[0] = int(H_ / 5) * 5
        iloc_of_beta_[1] = iloc_of_beta_[0] + 3
        H_current_[1] = int(H_ / 5) * 5 + 5
    elif H_ == 40:
        iloc_of_beta_[0] = int((H_ - 10) / 5) * 3 - 3
        H_current_[0] = 35
        iloc_of_beta_[1] = iloc_of_beta_[0] + 3
        H_current_[1] = 40
    else:
        raise ValueError(
            "Parameters error passed in \"get_iloc_of_beta\" function!\n\"get_iloc_of_beta\"函数传入的参数错误！")
    return iloc_of_beta_, H_current_


# 定义一个函数，根据一组 file_name, sheet_name, iloc_of_beta, beta 得到 delta
def get_iloc_by_single_group_paras(file_name_, sheet_name_, iloc_of_beta_, beta_):
    calc_data = pd.read_excel(file_name_, sheet_name=sheet_name_)
    beta_data = np.array(calc_data.iloc[:, iloc_of_beta_])
    # print("beta_data is", beta_data)
    delta_data = np.array(calc_data.iloc[:, iloc_of_beta_ + 1])
    # print("delta_data is", delta_data)
    delta_ = None
    for i in range(len(beta_data) - 1):
        if beta_ == 55:
            delta_ = delta_data[-1]
        if beta_data[i+1] > beta_ >= beta_data[i]:
            delta_ = (delta_data[i + 1] - delta_data[i]) / (beta_data[i + 1] - beta_data[i]) * (beta_ - beta_data[i]) + \
                     delta_data[i]
            break
    return delta_


# 定义一个函数，根据 alpha_w, r_u, H_star(这三个值必须是直接有的，不能是中间值), H, beta 得到 delta
def get_delta_by_H(alpha_w_, r_u_, H_star_, H_, beta_):
    # 获取Excel文件名和Sheet名
    file_name_, sheet_name_ = get_file_and_sheet_name(alpha_w_, r_u_, H_star_)
    # 针对不同的H值选择iloc
    iloc_of_beta_, H_current_ = get_iloc_of_beta(H_)
    # 按H值使用插值法计算delta
    delta_1_ = get_iloc_by_single_group_paras(file_name_, sheet_name_, iloc_of_beta_[0], beta_)
    # print("{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t\t{:.3f}".format(alpha_w_, r_u_, H_star_, H_, iloc_of_beta_[0], delta_1_))
    delta_2_ = get_iloc_by_single_group_paras(file_name_, sheet_name_, iloc_of_beta_[1], beta_)
    # print("{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t\t{:.3f}".format(alpha_w_, r_u_, H_star_, H_, iloc_of_beta_[1], delta_1_))
    # print("delta_1 and delta_2 is ", delta_1_, delta_2_, ", respectively")
    delta_ = (delta_2_ - delta_1_) / (H_current_[1] - H_current_[0]) * (H_ - H_current_[0]) + delta_1_
    # print(delta_)
    return delta_


if __name__ == "__main__":
    alpha_w = 0
    r_u = 0
    H_star = 1
    H = 37.5
    beta = 17.5

    # file_name, sheet_name = get_file_and_sheet_name(alpha_w, r_u, H_star)
    # # print(file_name, sheet_name)
    # iloc_of_beta, H_current = get_iloc_of_beta(H)
    # print(iloc_of_beta)
    # delta_1 = get_iloc_by_single_group_paras(file_name, sheet_name, iloc_of_beta[0], beta)
    # delta_2 = get_iloc_by_single_group_paras(file_name, sheet_name, iloc_of_beta[1], beta)
    # print("delta_1 and delta_2 is ", delta_1, delta_2, ", respectively")
    get_delta_by_H(alpha_w, r_u, H_star, H, beta)

