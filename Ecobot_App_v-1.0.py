import Main_Window
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime
import serial, time, sys, modules


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Main_Window.Ui_Form()
        self.ui.setupUi(self)
        self.ports = []
        self.loading_ports()
        self.a = modules.WidgetResults()
        self.b = modules.WidgetResearch(self.ports)
        self.c = modules.WidgetMap()        
        self.d = modules.WidgetInformation()
        self.ui.gridLayout.addWidget(modules.WidgetResearch(self.ports))
        self.ui.label_12.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.ui.pushButton_5.clicked.connect(self.results_command)
        self.ui.pushButton_6.clicked.connect(self.research_command)
        self.ui.pushButton_7.clicked.connect(self.map_command)
        self.ui.pushButton_8.clicked.connect(self.information_command)
    
    def load_data(self, sp):
        for i in range(1, 11):
            time.sleep(1)
            QtWidgets.qApp.processEvents()

    def results_command(self):
        self.ui.label_11.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.ui.label_12.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_13.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_14.setStyleSheet("background-color: rgb(36, 117, 164);")
        for i in reversed(range(self.ui.gridLayout.count())): 
            self.ui.gridLayout.itemAt(i).widget().setParent(None)
        self.ui.gridLayout.addWidget(self.a)

    def research_command(self):
        self.ui.label_11.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_12.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.ui.label_13.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_14.setStyleSheet("background-color: rgb(36, 117, 164);")

        for i in reversed(range(self.ui.gridLayout.count())): 
            self.ui.gridLayout.itemAt(i).widget().setParent(None)
        self.b = modules.WidgetResearch(self.ports)
        self.ui.gridLayout.addWidget(self.b)

    def map_command(self):
        self.ui.label_11.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_12.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_13.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_14.setStyleSheet("background-color: rgb(232, 232, 232);")

        for i in reversed(range(self.ui.gridLayout.count())): 
            self.ui.gridLayout.itemAt(i).widget().setParent(None)
        #self.a = modules.WidgetMap()
        self.ui.gridLayout.addWidget(self.c)

    def information_command(self):
        self.ui.label_11.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_12.setStyleSheet("background-color: rgb(36, 117, 164);")
        self.ui.label_13.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.ui.label_14.setStyleSheet("background-color: rgb(36, 117, 164);")
      
        for i in reversed(range(self.ui.gridLayout.count())): 
            self.ui.gridLayout.itemAt(i).widget().setParent(None)
        #self.a = modules.WidgetInformation()
        self.ui.gridLayout.addWidget(self.d)
    def loading_ports(self):
        for i in range(3,17):
            try:
                print(i)
                s = serial.Serial('COM'+str(i))
                self.ports.append(s.portstr)
                s.close() 
            except serial.SerialException:
                pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("Заставка1.jpg"))
    splash.show()
    QtWidgets.qApp.processEvents()
    window = MainWindow()
    window.setWindowTitle("Ecobot App")
    window.setWindowIcon(QIcon('em.ico'))
    window.load_data(splash)
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())