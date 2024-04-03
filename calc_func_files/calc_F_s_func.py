# -*- coding: utf-8 -*-
# @Time        : 2024/3/27 16:14
# @Author      : husky
# @FileName    : calc_F_s_func.py
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
from calc_func_files.calc_delta_func import get_delta_
from calc_func_files.calc_f_func import get_f_


def calc_F_s_func(r_u_, alpha_w_, c_, gamma_, H_, varphi_, beta_):
    f_ = get_f_(r_u_, alpha_w_, c_, gamma_, varphi_)
    delta_ = get_delta_(r_u_, alpha_w_, c_, gamma_, H_, varphi_, beta_)
    F_s_ = f_ * delta_
    print("f: {:.5f}\tdelta: {:.5f}\tF_s: {:.5f}".format(f_, delta_, F_s_))
    return f_, delta_, F_s_


if __name__ == "__main__":
    # r_u = 0
    # alpha_w = 0
    #
    # c = 28.9
    # gamma = 19.6
    # H = 20
    # varphi = 12.5
    # beta = 30

    # 1
    H, beta, c, varphi, gamma, r_u, alpha_w = 20, 30, 28.9, 12.5, 19.6, 0, 0
    # 1_25
    # H, beta, c, varphi, gamma, r_u, alpha_w = 25, 30, 28.9, 12.5, 19.6, 0, 0
    # 2
    # H, beta, c, varphi, gamma, r_u, alpha_w = 10, 45, 10, 45, 20, 0.25, 0
    # 3
    # H, beta, c, varphi, gamma, r_u, alpha_w = 15, 30, 25, 30, 16, 0, 0
    # 4
    # H, beta, c, varphi, gamma, r_u, alpha_w = 30, 35, 57.6, 16, 21.7, 0.15, 0
    # 5
    # H, beta, c, varphi, gamma, r_u, alpha_w = 15, 45, 85.6, 20, 19.6, 0.1, 0
    # 6
    # H, beta, c, varphi, gamma, r_u, alpha_w = 25, 50, 217.7, 25, 22.5, 0.2, 0
    # 7
    # H, beta, c, varphi, gamma, r_u, alpha_w = 35, 55, 401.8, 30, 23.3, 0, 0.05
    # 8
    # H, beta, c, varphi, gamma, r_u, alpha_w = 20, 50, 692.5, 35.7, 24.5, 0, 0.1
    # 9_完全案例
    # H, beta, c, varphi, gamma, r_u, alpha_w = 25, 35, 76.37, 15, 19, 0, 0

    F_s = calc_F_s_func(r_u, alpha_w, c, gamma, H, varphi, beta)

    # print("f: {:.5f}\tdelta: {:.5f}\tF_s: {:.5f}".)
