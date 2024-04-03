# -*- coding: utf-8 -*-
# @Time        : 2024/3/25 10:32
# @Author      : husky
# @FileName    : main.py.py
# @Software    : PyCharm
# @ProjectName : ICSS-Slope
# @Email       : shiguihuang1874@qq.com

"""
这是程序的入口
"""
from PyQt5.QtWidgets import QApplication

from rec_files.main_window_class import Main_Window_Pane

from rec_files import rec_rc

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.processEvents()
    MainWindow = Main_Window_Pane()
    MainWindow.show()
    # MainWindow.stability_pane.exit(app.exec_())
    sys.exit(app.exec_())
