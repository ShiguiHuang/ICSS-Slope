# -*- coding: utf-8 -*-
# @Time        : 2024/4/2 14:40
# @Author      : husky
# @FileName    : main_window_class.py
# @Software    : PyCharm
# @ProjectName : ICSS-Slope
# @Email       : shiguihuang1874@qq.com
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLabel, QStatusBar

from calc_func_files.calc_F_s_func import calc_F_s_func
from calc_func_files.check_paras_func import check_paras_func
from rec_files.MainWindow_ui import Ui_MainWindow


class Main_Window_Pane(QMainWindow, Ui_MainWindow):
    """继承主UI文件，作为程序的主类，连接各个部分。"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.statusBar = None
        self.setupUi(self)

        # 调用状态栏设置函数
        self.set_status_bar_func()

        # 定义需要的变量
        # 坡高 H
        self.H = 0
        # 坡角 beta
        self.beta = 0
        # 黏聚力 c
        self.c = 0
        # 重度 gamma
        self.gamma = 0
        # 内摩擦角 varphi
        self.varphi = 0
        # 地下水系数 r_u
        self.r_u = 0
        # 水平地震系数 alpha_w
        self.alpha_w = 0

        # 标准坡形下的安全系数 f
        self.f = 0
        # 坡形影响因子 delta
        self.delta = 0
        # 最终安全系数 F_S
        self.F_S = 0

    # 定义点击按钮后的操作
    def click_calc_PB(self):
        print("clac_PB is clicked!")
        # 1. 调用获取参数函数
        self.get_paras_func()
        # 2. 检查参数合理性
        check_re = self.check_paras_func()
        if check_re:
            return None
        # 3. 调用计算函数
        self.f, self.delta, self.F_S = calc_F_s_func(self.r_u, self.alpha_w, self.c, self.gamma, self.H, self.varphi,
                                                     self.beta)
        # 4. 赋值到控件
        self.set_result_func()

    # 定义获取参数的函数
    def get_paras_func(self):
        print("get paras!")
        self.H = self.H_DSB.value()
        self.beta = self.beta_DSB.value()
        self.c = self.c_DSB.value()
        self.gamma = self.gamma_DSB.value()
        self.varphi = self.varphi_DSB.value()
        self.r_u = self.r_u_DSB.value()
        self.alpha_w = self.alpha_w_DSB.value()

    # 定义检查参数的函数
    def check_paras_func(self):
        result = False
        check_result = check_paras_func(self.c, self.gamma, self.varphi, self.r_u, self.alpha_w)
        if not check_result[2]:
            reply = QMessageBox.warning(self, "警告",
                                        "gamma, varphi 不能为 0, 请修改 gamma, varphi 后重试！",
                                        QMessageBox.Yes, QMessageBox.Yes)
            result = True
            return result

        elif not check_result[1]:
            reply = QMessageBox.warning(self, "警告",
                                        "c, gamma, varphi 对应的等效高度大于 45，本程序无法计算，请减小 c, 或增大 gamma, varphi 后重试！",
                                        QMessageBox.Yes, QMessageBox.Yes)
            result = True
            return result

        elif not check_result[0]:
            reply = QMessageBox.warning(self, "警告",
                                        "c, gamma, varphi 对应的等效高度小于 0.25，本程序无法计算，请增大 c, 或减小 gamma, varphi 后重试！",
                                        QMessageBox.Yes, QMessageBox.Yes)
            result = True
            return result

        elif not check_result[3]:
            reply = QMessageBox.warning(self, "警告",
                                        "r_u 和 alpha_w 中必须有一个为 0，请修改后重试！",
                                        QMessageBox.Yes, QMessageBox.Yes)
            result = True
            return result

        else:
            return result

    # 定义一个复制函数
    def set_result_func(self):
        self.f_Label.setText("{:.3f}".format(self.f))
        self.delta_Label.setText("{:.3f}".format(self.delta))
        self.F_S_Label.setText("{:.3f}".format(self.F_S))

    # 定义一个设置状态栏的函数
    def set_status_bar_func(self):
        # 实例化状态栏
        # self.statusBar = QStatusBar(self)
        
        # 设置状态栏显示内容
        font = QFont("Times New Roman", 12)  # 设置字体为 Times New Roman，大小为 12
        font.setBold(True)  # 设置为加粗
        font.setItalic(True)  # 设置为斜体

        label = QLabel("KUST-Research Center of Deep Rock Engineering (昆明理工大学 -深地岩体工程研究中心)")
        label.setFont(font)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # 设置文本右对齐
        self.statusBar.addPermanentWidget(label)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.processEvents()
    MainWindow = Main_Window_Pane()
    MainWindow.show()
    # MainWindow.stability_pane.exit(app.exec_())
    sys.exit(app.exec_())
