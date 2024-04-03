# -*- coding: utf-8 -*-
# @Time        : 2024/3/27 14:17
# @Author      : husky
# @FileName    : calc_delta_from_H_star.py
# @Software    : PyCharm
# @ProjectName : ICSS-Slope
# @Email       : shiguihuang1874@qq.com

"""
该文件中的函数实现的功能为从指定(即是无需经过插值法)的 alpha_w, r_u 函数中计算与 H_star, H (需要经过插值法)相关的 delta
"""

from calc_func_files.calc_delta_from_H import get_delta_by_H


# 定义一个函数，根据 alpha_w, r_u(这两个值是必须有的，不能是中间值), H_star, H, beta 得到 delta
def get_delta_by_H_star(alpha_w_, r_u_, H_star_, H_, beta_):
    # 判断前后需要的 H_star_current 值
    H_star_current_ = [None, None]
    if 0.25 <= H_star_ < 1:
        H_star_current_ = [0.25, 1]
    elif 1 <= H_star_ < 3:
        H_star_current_ = [1, 3]
    elif 3 <= H_star_ < 5:
        H_star_current_ = [3, 5]
    elif 5 <= H_star_ < 15:
        H_star_current_ = [5, 15]
    elif 15 < H_star_ <= 35:
        H_star_current_ = [15, 35]
    elif 35 < H_star_ <= 45:
        H_star_current_ = [35, 45]
    else:
        raise ValueError(
            "Parameters error passed in \"get_delta_by_H_star\" function!\n\"get_delta_by_H_star\"函数传入的参数错误！")

    # 计算上下的两个 delta 值
    delta_1_ = get_delta_by_H(alpha_w_, r_u_, H_star_current_[0], H_, beta_)
    print("{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t\t{:.5f}".format(alpha_w_, r_u_, H_star_current_[0], H_, beta_, delta_1_))
    delta_2_ = get_delta_by_H(alpha_w_, r_u_, H_star_current_[1], H_, beta_)
    print("{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t\t{:.5f}".format(alpha_w_, r_u_, H_star_current_[1], H_, beta_, delta_2_))
    # print("delta_1 and delta_2 is ", delta_1_, delta_2_, ", respectively")
    # 利用插值法求 H_star_ 对应的 delta_
    delta_ = (delta_2_ - delta_1_) / (H_star_current_[1] - H_star_current_[0]) * (H_star_ - H_star_current_[0]) + delta_1_
    return delta_


if __name__ == "__main__":
    alpha_w = 0
    r_u = 0
    H_star = 8
    H = 37.5
    beta = 17.5
    print(get_delta_by_H_star(alpha_w, r_u, H_star, H, beta))
