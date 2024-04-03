# -*- coding: utf-8 -*-
# @Time        : 2024/3/27 14:49
# @Author      : husky
# @FileName    : calc_delta_from_r_u_alpha_w.py
# @Software    : PyCharm
# @ProjectName : ICSS-Slope
# @Email       : shiguihuang1874@qq.com

"""
该文件中的函数实现的功能为从 alpha_w, r_u, H_star, H (需要经过插值法)相关的 delta
"""
from calc_func_files.calc_delta_from_H_star import get_delta_by_H_star


# 定义一个函数，用来计算当 r_u==0 时的 delta
def get_delta_when_r_u_0(alpha_w_, r_u_, H_star_, H_, beta_):
    # 检查 r_u_ 是否为 0
    if r_u_ != 0:
        raise ValueError("One of alpha_w and r_u must be 0!")

    # 确定 alpha_w_current_ 的 上下限
    if 0 <= alpha_w_ <= 0.05:
        alpha_w_current_ = [0.0, 0.05]
    elif 0.05 < alpha_w_ <= 0.10:
        alpha_w_current_ = [0.05, 0.10]
    else:
        raise ValueError("alpha_w not in 0 ~ 0.1!")

    # 计算上下的两个 delta 值
    delta_1_ = get_delta_by_H_star(alpha_w_current_[0], r_u_, H_star_, H_, beta_)
    delta_2_ = get_delta_by_H_star(alpha_w_current_[1], r_u_, H_star_, H_, beta_)

    # 使用插值法计算最终的 delta_
    delta_ = (delta_2_ - delta_1_) / (alpha_w_current_[1] - alpha_w_current_[0]) * (alpha_w_ - alpha_w_current_[0]) + delta_1_

    return delta_


# 定义一个函数，用来计算当 alpha_w_==0 时的 delta
def get_delta_when_alpha_w_0(alpha_w_, r_u_, H_star_, H_, beta_):
    # 检查 alpha_w_ 是否为 0
    if alpha_w_ != 0:
        raise ValueError("One of alpha_w and r_u must be 0!")

    # 确定 r_u_current_ 的上下限
    if 0.0 <= r_u_ <= 0.25:
        r_u_current_ = [0.0, 0.25]
    elif 0.25 < r_u_ <= 0.50:
        r_u_current_ = [0.25, 0.50]
    else:
        raise ValueError("r_u not in 0 ~ 0.5!")

    # 计算上下的两个 delta 值
    delta_1_ = get_delta_by_H_star(alpha_w_, r_u_current_[0], H_star_, H_, beta_)
    print("{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t\t{:.6f}".format(alpha_w_, r_u_current_[0], H_star_, H_, beta_, delta_1_))
    delta_2_ = get_delta_by_H_star(alpha_w_, r_u_current_[1], H_star_, H_, beta_)
    print("{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t\t{:.6f}".format(alpha_w_, r_u_current_[1], H_star_, H_, beta_, delta_2_))

    # 使用差值法计算最终的 delta_
    delta_ = (delta_2_ - delta_1_) / (r_u_current_[1] - r_u_current_[0]) * (r_u_ - r_u_current_[0]) + delta_1_
    return delta_


# 定义一个函数，根据 alpha_w, r_u, H_star, H, beta 得到 delta
def get_delta_by_alpha_w_r_u(alpha_w_, r_u_, H_star_, H_, beta_):
    if alpha_w_ == 0:
        delta_ = get_delta_when_alpha_w_0(alpha_w_, r_u_, H_star_, H_, beta_)
    else:
        delta_ = get_delta_when_r_u_0(alpha_w_, r_u_, H_star_, H_, beta_)

    return delta_


if __name__ == "__main__":
    alpha_w = 0
    r_u = 0.5
    H_star = 8
    H = 37.5
    beta = 17.5
    print(get_delta_by_alpha_w_r_u(alpha_w, r_u, H_star, H, beta))
