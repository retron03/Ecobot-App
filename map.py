# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map.ui'
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
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
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
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);\n"
"    font: 8pt \"Arial Rounded MT Bold\";\n"
"}\n"
"QLineEdit{\n"
"\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 3px;\n"
"}\n"
"QPlainTextEdit{\n"
"    background-color: rgb(56, 56, 56);\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, -10, 851, 531))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(536, 23, 121, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(536, 48, 121, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 651, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_9 = QtWidgets.QFrame(self.widget)
        self.frame_9.setGeometry(QtCore.QRect(10, 20, 521, 51))
        self.frame_9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.471591 rgba(29, 96, 135, 255), stop:0.784091 rgba(34, 125, 200, 255));\n"
"border-radius: 7px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 20, 171, 21))
        self.lineEdit_3.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 3px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 20, 121, 21))
        self.lineEdit_4.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 3px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_18 = QtWidgets.QLabel(self.frame_9)
        self.label_18.setGeometry(QtCore.QRect(10, 3, 91, 16))
        self.label_18.setStyleSheet("background-color: rgba(36, 36, 36, 0);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_9)
        self.label_19.setGeometry(QtCore.QRect(340, 4, 91, 16))
        self.label_19.setStyleSheet("background-color: rgba(36, 36, 36, 0);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_9)
        self.label_20.setGeometry(QtCore.QRect(210, 3, 111, 16))
        self.label_20.setStyleSheet("background-color: rgba(36, 36, 36, 0);")
        self.label_20.setObjectName("label_20")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_9)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 20, 194, 22))
        self.dateTimeEdit.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 3px;")
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Отметить точки"))
        self.pushButton_2.setText(_translate("Form", "Очистить карту"))
        self.label_18.setText(_translate("Form", "Дата и время "))
        self.label_19.setText(_translate("Form", "Локация"))
        self.label_20.setText(_translate("Form", "Название водоема "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
