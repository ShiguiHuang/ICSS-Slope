# -*- coding: utf-8 -*-
# @Time        : 2024/3/27 15:39
# @Author      : husky
# @FileName    : calc_delta_func.py
# @Software    : PyCharm
# @ProjectName : ICSS-Slope
# @Email       : shiguihuang1874@qq.com


"""
输入的参数为：
坡高： H

黏聚力：c
重度： gamma
内摩擦角：varphi

地下水系数：r_u
水平地震系数：alpha_w
"""
import numpy as np

from calc_func_files.calc_delta_from_r_u_alpha_w import get_delta_by_alpha_w_r_u


# 定义获取 delta 的函数
def get_delta_(r_u_, alpha_w_, c_, gamma_, H_, varphi_, beta_):
    varphi_rad_ = np.radians(varphi_)

    H_star_ = c_ / (gamma_ * np.tan(varphi_rad_))
    print("H_star is", H_star_)
    print("alpha_w\tr_u\t\tH_star\tH\t\tbeta\t\tdelta")

    delta_ = get_delta_by_alpha_w_r_u(alpha_w_, r_u_, H_star_, H_, beta_)

    return delta_


if __name__ == "__main__":
    # r_u = 0
    # alpha_w = 0
    #
    # c = 28.9
    # gamma = 19.6
    # H = 20
    # varphi = 12.5
    # beta = 30

    H, beta, c, varphi, gamma, r_u, alpha_w = 10, 45, 10, 45, 20, 0.25, 0

    delta = get_delta_(r_u, alpha_w, c, gamma, H, varphi, beta)

    print(delta)
