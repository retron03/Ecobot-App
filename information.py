# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information.ui'
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
"\n"
"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel{\n"
"background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 3px;\n"
"}\n"
"QPlainTextEdit{\n"
"    background-color: rgb(56, 56, 56);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, -10, 851, 531))
        self.widget.setObjectName("widget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 651, 461))
        self.textBrowser.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color:rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Наш проект посвящен созданию мобильной лаборатории для мониторинга малых водоемов естественного и искусственного происхождения. Проект имеет большую практическую значимость, потому что проблема загрязнения водоемов стоит остро по всему миру. На данный момент нами сконструирована модель мобильной лаборатории, разработаны программное обеспечение и канал передачи данных от плавучей платформы к стационарному операторскому пункту. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Версия приложения: 1.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">В обновлении  2.0 будут осуществлены изменения, которые позволят взаимодействовать с нашим вебсервером, давая  возможность хранить данные ваших исследований в облачном хранилице проекта Ecobot.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
