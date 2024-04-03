# -*- coding: utf-8 -*-
# @Time        : 2024/4/1 19:26
# @Author      : husky
# @FileName    : check_paras_func.py
# @Software    : PyCharm
# @ProjectName : ICSS-Slope
# @Email       : shiguihuang1874@qq.com

import numpy as np


# 定义一个参数检查函数
def check_paras_func(c_, gamma_, varphi_, r_u_, alpha_w_):
    """
    参数检查函数
    由于其他参数有指定范围，可在界面输入时对其进行限定，因此不必在此进行检查
    :param c_: float, 黏聚力
    :param gamma_: float, 容重
    :param varphi_: float, 内摩擦角
    :return:
        list, 检查结果
        如果：
            check_result[0] == False, 参数 黏聚力、容重和内摩擦角构成的等效高度小于指定范围
            check_result[1] == False, 参数 黏聚力、容重和内摩擦角构成的等效高度大于指定范围
            check_result[2] == False, gamma 和 varphi 不能为 0
    """
    check_result = [True, True, True, True]

    # 检查 黏聚力 c_, 容重 gamma_, 内摩擦角 c_
    if gamma_ == 0 or varphi_ == 0:
        check_result[2] = False
        return check_result

    H_star = c_ / (gamma_ * np.tan(np.radians(varphi_)))
    if H_star < 0.25:
        check_result[0] = False
    if H_star > 45:
        check_result[1] = False
    if alpha_w_ != 0 and r_u_ != 0:
        check_result[3] = False

    return check_result


if __name__ == "__main__":
    H, beta, c, gamma, varphi, r_u, alpha_w = [5, 5, 0, 10, 21, -0.1, 0.7]
    print(check_paras_func(c, gamma, varphi))
