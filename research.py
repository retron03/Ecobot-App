# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'research.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 480)
        Form.setMinimumSize(QtCore.QSize(670, 480))
        Form.setMaximumSize(QtCore.QSize(670, 480))
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"QPushButton{\n"
"    font: 50 8pt \"MS Shell Dlg 2\";\n"
"    border-radius: 3px;\n"
"    color:rgb(255, 255, 255);\n"
"    background-color: rgb(36, 117, 164);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(37, 129, 179);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(27, 92, 129);\n"
"}\n"
"\n"
"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"        font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);\n"
"        font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 3px;\n"
"}\n"
"QPlainTextEdit{\n"
"    background-color: rgb(56, 56, 56);\n"
"        font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, -30, 1031, 551))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(300, 63, 371, 131))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.471591 rgba(29, 96, 135, 255), stop:0.784091 rgba(34, 125, 200, 255));\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label_5.setStyleSheet("background-color: rgb(29, 96, 135);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 61, 21))
        self.label_6.setStyleSheet("background-color: rgb(29, 96, 135);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 20, 241, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 50, 241, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 80, 241, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(36, 36,36);\n"
"selection-background-color: rgb(36, 36, 36);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 41, 21))
        self.label_8.setStyleSheet("background-color: rgb(29, 96, 135);")
        self.label_8.setObjectName("label_8")
        self.line_15 = QtWidgets.QFrame(self.frame)
        self.line_15.setGeometry(QtCore.QRect(12, 10, 118, 3))
        self.line_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.frame)
        self.line_16.setGeometry(QtCore.QRect(80, 10, 118, 3))
        self.line_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.frame)
        self.line_17.setGeometry(QtCore.QRect(240, 10, 118, 3))
        self.line_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.frame)
        self.line_18.setGeometry(QtCore.QRect(130, 10, 118, 3))
        self.line_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.frame)
        self.line_19.setGeometry(QtCore.QRect(240, 110, 118, 3))
        self.line_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.frame)
        self.line_20.setGeometry(QtCore.QRect(130, 110, 118, 3))
        self.line_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.frame)
        self.line_21.setGeometry(QtCore.QRect(80, 110, 118, 3))
        self.line_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.frame)
        self.line_22.setGeometry(QtCore.QRect(12, 110, 118, 3))
        self.line_22.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setGeometry(QtCore.QRect(20, 270, 271, 211))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.471591 rgba(29, 96, 135, 255), stop:0.784091 rgba(34, 125, 200, 255));\n"
"border-radius: 7px;\n"
"border-radius: 7px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.line_23 = QtWidgets.QFrame(self.frame_3)
        self.line_23.setGeometry(QtCore.QRect(10, 10, 118, 3))
        self.line_23.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.frame_3)
        self.line_24.setGeometry(QtCore.QRect(110, 10, 118, 3))
        self.line_24.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_10.setStyleSheet("background-color: rgb(29, 96, 135);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(160, 110, 101, 16))
        self.label_11.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.label_12.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_12.setObjectName("label_12")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(10, 40, 251, 91))
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 7px;\n"
"}\n"
"QLabel{\n"
"background-color: rgb(36, 36, 36);\n"
"\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_14.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 131, 16))
        self.label_13.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(150, 10, 91, 16))
        self.label_15.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(150, 30, 91, 16))
        self.label_16.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(150, 50, 91, 16))
        self.label_17.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_18.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_18.setObjectName("label_18")
        self.line_29 = QtWidgets.QFrame(self.frame_3)
        self.line_29.setGeometry(QtCore.QRect(143, 10, 118, 3))
        self.line_29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(20, 137, 141, 71))
        self.label_20.setStyleSheet("font: 32pt \"Arial Rounded MT Bold\";\n"
"background: rgba(255,255,255,0);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(179, 137, 71, 71))
        self.label.setStyleSheet("border-image: url(:/newPrefix/SSun.jpg);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.line_23.raise_()
        self.line_24.raise_()
        self.label_10.raise_()
        self.frame_4.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.line_29.raise_()
        self.label_20.raise_()
        self.label.raise_()
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 110, 271, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 63, 271, 31))
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(300, 220, 371, 261))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.471591 rgba(29, 96, 135, 255), stop:0.784091 rgba(34, 125, 200, 255));\n"
"border-radius: 7px;\n"
"border-radius: 7px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line_25 = QtWidgets.QFrame(self.frame_2)
        self.line_25.setGeometry(QtCore.QRect(10, 10, 118, 3))
        self.line_25.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.frame_2)
        self.line_26.setGeometry(QtCore.QRect(120, 10, 118, 3))
        self.line_26.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.frame_2)
        self.line_27.setGeometry(QtCore.QRect(150, 10, 118, 3))
        self.line_27.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.frame_2)
        self.line_28.setGeometry(QtCore.QRect(243, 10, 118, 3))
        self.line_28.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.label_9.setStyleSheet("background-color: rgb(29, 96, 135);")
        self.label_9.setObjectName("label_9")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 50, 351, 201))
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 7px;\n"
"}\n"
"QLabel{\n"
"background-color: rgb(36, 36, 36);\n"
"\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(20, 46, 131, 16))
        self.label_21.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(20, 70, 151, 16))
        self.label_22.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_23.setGeometry(QtCore.QRect(200, 20, 91, 16))
        self.label_23.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setGeometry(QtCore.QRect(200, 45, 91, 16))
        self.label_24.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_5)
        self.label_25.setGeometry(QtCore.QRect(200, 70, 91, 16))
        self.label_25.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        self.label_26.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_26.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_5)
        self.label_27.setGeometry(QtCore.QRect(20, 93, 151, 16))
        self.label_27.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_5)
        self.label_28.setGeometry(QtCore.QRect(200, 93, 91, 16))
        self.label_28.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_5)
        self.label_29.setGeometry(QtCore.QRect(20, 115, 161, 16))
        self.label_29.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_5)
        self.label_30.setGeometry(QtCore.QRect(201, 140, 91, 16))
        self.label_30.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_5)
        self.label_31.setGeometry(QtCore.QRect(201, 117, 91, 16))
        self.label_31.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(31, 157, 251, 20))
        self.comboBox_3.setStyleSheet("background-color: rgb(36, 36,36);\n"
"selection-background-color: rgb(36, 36, 36);\n"
"border-radius: 3px;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.frame_8 = QtWidgets.QFrame(self.widget)
        self.frame_8.setGeometry(QtCore.QRect(20, 152, 271, 51))
        self.frame_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.471591 rgba(29, 96, 135, 255), stop:0.784091 rgba(34, 125, 200, 255));\n"
"border-radius: 7px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(31, 179, 251, 21))
        self.lineEdit_5.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(22, 220, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_32 = QtWidgets.QLabel(self.widget)
        self.label_32.setGeometry(QtCore.QRect(90, 224, 121, 16))
        self.label_32.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.label_32.setObjectName("label_32")
        self.frame.raise_()
        self.frame_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.frame_2.raise_()
        self.frame_8.raise_()
        self.comboBox_3.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_3.raise_()
        self.label_32.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Локация"))
        self.label_6.setText(_translate("Form", "Название "))
        self.comboBox_2.setItemText(0, _translate("Form", "Озеро"))
        self.comboBox_2.setItemText(1, _translate("Form", "Водохранилище"))
        self.comboBox_2.setItemText(2, _translate("Form", "Пруд"))
        self.label_8.setText(_translate("Form", "Класс"))
        self.label_10.setText(_translate("Form", "Погода в регионе"))
        self.label_12.setText(_translate("Form", "Скорость ветра - "))
        self.label_14.setText(_translate("Form", "Состояние погоды -"))
        self.label_13.setText(_translate("Form", "Давление - "))
        self.label_18.setText(_translate("Form", "Влажность - "))
        self.pushButton_2.setText(_translate("Form", "Завершить исследование"))
        self.pushButton.setText(_translate("Form", "Начать исследование"))
        self.label_9.setText(_translate("Form", "Данные исследования "))
        self.label_21.setText(_translate("Form", "Значение PH - "))
        self.label_22.setText(_translate("Form", "Температура воды - "))
        self.label_26.setText(_translate("Form", "Мутность воды - "))
        self.label_27.setText(_translate("Form", "Температура воздуха - "))
        self.label_29.setText(_translate("Form", "Географические координаты- "))
        self.comboBox_3.setItemText(0, _translate("Form", "Выберите COM- порт"))
        self.pushButton_3.setText(_translate("Form", "Обновить"))
        self.label_32.setText(_translate("Form", "Обновить Com- порты"))
import Source_widget_1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
