# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(979, 715)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.centralwidget.setFont(font)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.H_DSB = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.H_DSB.setMinimumSize(QtCore.QSize(0, 25))
        self.H_DSB.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.H_DSB.setFont(font)
        self.H_DSB.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.H_DSB.setStyleSheet("background-color: rgb(255,255,255);")
        self.H_DSB.setPrefix("")
        self.H_DSB.setSuffix("")
        self.H_DSB.setDecimals(2)
        self.H_DSB.setMinimum(10.0)
        self.H_DSB.setMaximum(40.0)
        self.H_DSB.setObjectName("H_DSB")
        self.horizontalLayout_2.addWidget(self.H_DSB)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.beta_DSB = QtWidgets.QDoubleSpinBox(self.widget_7)
        self.beta_DSB.setMinimumSize(QtCore.QSize(0, 25))
        self.beta_DSB.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.beta_DSB.setFont(font)
        self.beta_DSB.setStyleSheet("background-color: rgb(255,255,255);")
        self.beta_DSB.setDecimals(2)
        self.beta_DSB.setMinimum(15.0)
        self.beta_DSB.setMaximum(55.0)
        self.beta_DSB.setObjectName("beta_DSB")
        self.horizontalLayout_4.addWidget(self.beta_DSB)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.c_DSB = QtWidgets.QDoubleSpinBox(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.c_DSB.sizePolicy().hasHeightForWidth())
        self.c_DSB.setSizePolicy(sizePolicy)
        self.c_DSB.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.c_DSB.setFont(font)
        self.c_DSB.setStyleSheet("background-color: rgb(255,255,255);")
        self.c_DSB.setDecimals(2)
        self.c_DSB.setMaximum(99999.0)
        self.c_DSB.setObjectName("c_DSB")
        self.horizontalLayout_3.addWidget(self.c_DSB)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gamma_DSB = QtWidgets.QDoubleSpinBox(self.widget_8)
        self.gamma_DSB.setMinimumSize(QtCore.QSize(0, 25))
        self.gamma_DSB.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.gamma_DSB.setFont(font)
        self.gamma_DSB.setStyleSheet("background-color: rgb(255,255,255);")
        self.gamma_DSB.setDecimals(2)
        self.gamma_DSB.setMaximum(99999.0)
        self.gamma_DSB.setObjectName("gamma_DSB")
        self.horizontalLayout_5.addWidget(self.gamma_DSB)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.varphi_DSB = QtWidgets.QDoubleSpinBox(self.widget_9)
        self.varphi_DSB.setMinimumSize(QtCore.QSize(0, 25))
        self.varphi_DSB.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.varphi_DSB.setFont(font)
        self.varphi_DSB.setStyleSheet("background-color: rgb(255,255,255);")
        self.varphi_DSB.setDecimals(2)
        self.varphi_DSB.setMaximum(89.0)
        self.varphi_DSB.setObjectName("varphi_DSB")
        self.horizontalLayout_6.addWidget(self.varphi_DSB)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.r_u_DSB = QtWidgets.QDoubleSpinBox(self.widget_10)
        self.r_u_DSB.setMinimumSize(QtCore.QSize(0, 25))
        self.r_u_DSB.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.r_u_DSB.setFont(font)
        self.r_u_DSB.setStyleSheet("background-color: rgb(255,255,255);")
        self.r_u_DSB.setDecimals(3)
        self.r_u_DSB.setMaximum(0.5)
        self.r_u_DSB.setSingleStep(0.05)
        self.r_u_DSB.setObjectName("r_u_DSB")
        self.horizontalLayout_7.addWidget(self.r_u_DSB)
        self.verticalLayout_2.addWidget(self.widget_10)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.widget_11 = QtWidgets.QWidget(self.widget)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.alpha_w_DSB = QtWidgets.QDoubleSpinBox(self.widget_11)
        self.alpha_w_DSB.setMinimumSize(QtCore.QSize(0, 25))
        self.alpha_w_DSB.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.alpha_w_DSB.setFont(font)
        self.alpha_w_DSB.setStyleSheet("background-color: rgb(255,255,255);")
        self.alpha_w_DSB.setDecimals(3)
        self.alpha_w_DSB.setMaximum(0.1)
        self.alpha_w_DSB.setSingleStep(0.01)
        self.alpha_w_DSB.setObjectName("alpha_w_DSB")
        self.horizontalLayout_8.addWidget(self.alpha_w_DSB)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.calc_PB = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calc_PB.setFont(font)
        self.calc_PB.setStyleSheet("background-color: rgb(232, 230, 255);")
        self.calc_PB.setObjectName("calc_PB")
        self.verticalLayout_2.addWidget(self.calc_PB)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_12.setFont(font)
        self.label_12.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.widget_15 = QtWidgets.QWidget(self.widget_4)
        self.widget_15.setStyleSheet("image: url(:/img/model.png);")
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_4.addWidget(self.widget_15)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.widget_12 = QtWidgets.QWidget(self.widget_3)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setContentsMargins(6, 6, 0, 6)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_16 = QtWidgets.QLabel(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_16.setFont(font)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_16.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_16.setScaledContents(False)
        self.label_16.setWordWrap(False)
        self.label_16.setOpenExternalLinks(False)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.f_Label = QtWidgets.QLabel(self.widget_12)
        self.f_Label.setMaximumSize(QtCore.QSize(86, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.f_Label.setFont(font)
        self.f_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.f_Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.f_Label.setText("")
        self.f_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.f_Label.setObjectName("f_Label")
        self.horizontalLayout_9.addWidget(self.f_Label)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.widget_3)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_10.setContentsMargins(6, 6, 0, 6)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_17 = QtWidgets.QLabel(self.widget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_17.setScaledContents(False)
        self.label_17.setWordWrap(False)
        self.label_17.setOpenExternalLinks(False)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.delta_Label = QtWidgets.QLabel(self.widget_13)
        self.delta_Label.setMaximumSize(QtCore.QSize(86, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delta_Label.setFont(font)
        self.delta_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.delta_Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delta_Label.setText("")
        self.delta_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.delta_Label.setObjectName("delta_Label")
        self.horizontalLayout_10.addWidget(self.delta_Label)
        self.verticalLayout_3.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.widget_3)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_11.setContentsMargins(6, 6, 0, 6)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(self.widget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_18.setScaledContents(False)
        self.label_18.setWordWrap(False)
        self.label_18.setOpenExternalLinks(False)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.F_S_Label = QtWidgets.QLabel(self.widget_14)
        self.F_S_Label.setMaximumSize(QtCore.QSize(86, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F_S_Label.setFont(font)
        self.F_S_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.F_S_Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.F_S_Label.setText("")
        self.F_S_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.F_S_Label.setObjectName("F_S_Label")
        self.horizontalLayout_11.addWidget(self.F_S_Label)
        self.verticalLayout_3.addWidget(self.widget_14)
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 2)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.calc_PB.clicked.connect(MainWindow.click_calc_PB) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ICSS-Slope (基于坡形影响因子的边坡安全系数计算软件)"))
        self.label.setText(_translate("MainWindow", "Input parameters of slope (输入边坡参数)"))
        self.label_2.setText(_translate("MainWindow", "Height of slope (坡高) *H*："))
        self.label_9.setText(_translate("MainWindow", "(Range of value (取值范围)：10~40 m)"))
        self.label_3.setText(_translate("MainWindow", "Angle of slope (坡角) *β*："))
        self.label_11.setText(_translate("MainWindow", "(Range of value (取值范围)：15~55°)"))
        self.label_4.setText(_translate("MainWindow", "Cohesion (黏聚力) *c*："))
        self.label_5.setText(_translate("MainWindow", "Gravity (重度) *γ*："))
        self.label_6.setText(_translate("MainWindow", "Angle of internal friction (内摩擦角) *φ*："))
        self.label_7.setText(_translate("MainWindow", "Groundwater coefficient (地下水系数) *r*<sub>u</sub>："))
        self.label_14.setText(_translate("MainWindow", "(Range of value (取值范围)：0~0.5)"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Horizonal seimic coefficient (水平地震系数) <span style=\" font-style:italic;\">α</span><span style=\" vertical-align:sub;\">w</span>：</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "(Range of value (取值范围)：0~0.1)"))
        self.calc_PB.setText(_translate("MainWindow", "Input is completed, click to calculate!\n"
" (输入完成，点击进行计算!)"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Slope geometry and parameters diagram</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">(边坡几何及参数示意图)</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Result of calculation (计算结果)</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "Factor of safety with standard slope shape (标准坡形下的安全系数) *f*："))
        self.label_17.setText(_translate("MainWindow", "Influence coefficient of slope shape (坡形影响因子系数) *δ*："))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>Final slope factor of safety (最终安全系数) <span style=\" font-style:italic;\">F</span><span style=\" vertical-align:sub;\">S</span>：</p></body></html>"))
from rec_files import rec_rc