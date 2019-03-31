# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dilidili.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#这个是GUI界面架构程序，由qt designer生成的ui文件转化而来
#
class Ui_dilidili(object):
    def setupUi(self, dilidili):
        dilidili.setObjectName("dilidili")
        dilidili.resize(800, 600)
        #这是button的配置
        self.btnClear = QtWidgets.QPushButton(dilidili)
        self.btnClear.setGeometry(QtCore.QRect(700, 520, 93, 28))
        self.btnClear.setObjectName("btnClear")
        self.btnQuery = QtWidgets.QPushButton(dilidili)
        self.btnQuery.setGeometry(QtCore.QRect(600, 520, 93, 28))
        self.btnQuery.setObjectName("btnQuery")
        #这是groupBox的配置
        self.groupBox = QtWidgets.QGroupBox(dilidili)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 611, 431))
        self.groupBox.setObjectName("groupBox")
        #这是下拉框的配置
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 30, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 41, 20))
        self.label.setObjectName("label")
        
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(5, 80, 606, 400))
        self.resultText.setObjectName("resultText")
        

        self.retranslateUi(dilidili)
        #这是表征信号的操作，设置槽
        self.btnQuery.clicked.connect(dilidili.queryAnime)
        self.btnClear.clicked.connect(dilidili.clearResult)
        QtCore.QMetaObject.connectSlotsByName(dilidili)

        
    def retranslateUi(self, dilidili):
        _translate = QtCore.QCoreApplication.translate
        dilidili.setWindowTitle(_translate("dilidili", "D站番剧更新"))
        self.btnClear.setText(_translate("dilidili", "清空"))
        self.btnQuery.setText(_translate("dilidili", "查询"))
        self.groupBox.setTitle(_translate("dilidili", "番剧更新"))
        self.comboBox.setItemText(0, _translate("dilidili", "周一"))
        self.comboBox.setItemText(1, _translate("dilidili", "周二"))
        self.comboBox.setItemText(2, _translate("dilidili", "周三"))
        self.comboBox.setItemText(3, _translate("dilidili", "周四"))
        self.comboBox.setItemText(4, _translate("dilidili", "周五"))
        self.comboBox.setItemText(5, _translate("dilidili", "周六"))
        self.comboBox.setItemText(6, _translate("dilidili", "周日"))
        self.label.setText(_translate("dilidili", "日期"))

