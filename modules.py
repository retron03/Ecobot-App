from PyQt5 import QtWidgets, QtGui, QtCore, QtQuickWidgets, QtPositioning, QtPositioning
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from datetime import datetime
import First_App_Edition, result, map, information, research, weather
import serial, time, os, sys, random, sqlite3
from PyQt5.QtGui import QPixmap

class MyThread(QtCore.QThread,):

    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.input_data = ''
        self.p = ''
        self.port = ''

    def run(self):
        try:
            last = 'nothing'
            bluetooth = serial.Serial(self.port, 9600)
            bluetooth.flushInput()
            self.mysignal.emit("Успешное подключение")
            self.running = True
            while self.running:
                bluetooth.write(b"signal")
                self.input_data = bluetooth.readline()
                self.p = self.input_data.decode()
                if self.p != last:
                    print(self.p)
                    last = self.p
                    self.mysignal.emit("%s" % self.p)
                time.sleep(0.2)
            bluetooth.close()
        except:
            self.mysignal.emit("Ошибка соединения")
            self.running = False





class MarkerModel(QtCore.QAbstractListModel):
    PositionRole, SourceRole = range(QtCore.Qt.UserRole, QtCore.Qt.UserRole + 2)

    def __init__(self, parent=None):
        super(MarkerModel, self).__init__(parent)
        self._markers = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._markers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount():
            if role == MarkerModel.PositionRole:
                return self._markers[index.row()]["position"]
            elif role == MarkerModel.SourceRole:
                return self._markers[index.row()]["source"]
        return QtCore.QVariant()

    def roleNames(self):
        return {MarkerModel.PositionRole: b"position_marker", MarkerModel.SourceRole: b"source_marker"}

    def appendMarker(self, marker):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self._markers.append(marker)
        self.endInsertRows()


class MapWidget(QtQuickWidgets.QQuickWidget):
    def __init__(self, parent=None):
        super(MapWidget, self).__init__(parent,
            resizeMode=QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.model = MarkerModel(self)
        self.rootContext().setContextProperty("markermodel", self.model)
        qml_path = os.path.join(os.path.dirname(__file__), "C:\\Codepython\\My_app_project\\Ecobot\\Untitled-1.qml")
        self.setSource(QtCore.QUrl.fromLocalFile(qml_path))
      
    
    def place_marks(self, positions):
        urls = ["http://maps.gstatic.com/mapfiles/ridefinder-images/mm_20_gray.png", 
            "http://maps.gstatic.com/mapfiles/ridefinder-images/mm_20_red.png"]
        for c, u in zip(positions, urls):
            coord = QtPositioning.QGeoCoordinate(*c)
            source = QtCore.QUrl(u)
            self.model.appendMarker({"position": coord , "source": source})

class WidgetResearch(QtWidgets.QWidget):
    def __init__(self, ports,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.con = sqlite3.connect("app.db")
        self.cur = self.con.cursor()
        arr = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        self.string = ''
        self.ui = research.Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox_3.clear()
        for i in ports:
            self.ui.comboBox_3.addItem(i)
        self.mythread = MyThread()
        self.ui.pushButton.clicked.connect(self.begin_connection)
        self.ui.pushButton_2.clicked.connect(self.end_connection)
        self.ui.pushButton_3.clicked.connect(self.loading_ports)
        self.mythread.mysignal.connect(
            self.on_changed, QtCore.Qt.QueuedConnection)


    def loading_ports(self):
        self.ui.comboBox_3.clear()
        for i in range(3, 17):
            try:
                print(i)
                s = serial.Serial('COM'+str(i))
                self.ui.comboBox_3.addItem(s.portstr)
                s.close()
            except serial.SerialException:
                pass

    def begin_connection(self):
        try:
            self.con = sqlite3.connect("app.db")
            self.cur = self.con.cursor()
            self.string = str(datetime.strftime(datetime.now(), "%d.%m.%Y"))+"_"+str(datetime.strftime(datetime.now(), "%H:%M")) + \
                "_" + self.ui.lineEdit_3.text().replace(" ", "")+"_" + \
                str(self.ui.lineEdit_4.text().replace(" ", ""))
            sql = """\
                CREATE TABLE '{}' (TIME TEXT, PH TEXT, TURBIDITY TEXT, TEMPA TEXT, TEMPW TEXT, LONG TEXT, LAT TEXT) 
            """
            sql = sql.format(self.string.upper())
            self.cur.execute(sql)
            self.ui.pushButton.setDisabled(True)
            self.ui.pushButton_3.setDisabled(True)
            self.ui.lineEdit_3.setReadOnly(True)
            self.ui.lineEdit_4.setReadOnly(True)
            self.ui.lineEdit_5.setReadOnly(True)
            global indicator
            indicator = 0
            self.mythread.port = self.ui.comboBox_3.currentText()
            print(self.mythread.port)
            if not self.mythread.isRunning():
                self.mythread.start()
        except:
            pass

    def end_connection(self):
        if self.mythread.running:
            self.mythread.running = False
        global indicator
        indicator = 1
        self.ui.lineEdit_3.setReadOnly(False)
        self.ui.lineEdit_4.setReadOnly(False)
        self.ui.lineEdit_5.setReadOnly(False)
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton_3.setDisabled(False)

    def on_changed(self, s):
        global ind
        if s == "Ошибка соединения":
            self.ui.pushButton.setDisabled(False)
            self.ui.pushButton_3.setDisabled(False)
            self.ui.lineEdit_3.setReadOnly(False)
            self.ui.lineEdit_4.setReadOnly(False)
            self.ui.lineEdit_5.setReadOnly(False)
            self.ui.lineEdit_5.setText(s)
        else:
            sql = """\
                INSERT  INTO '{}' VALUES(:time , :ph, :turbidity, :tempa, :tempw, :long, :lat)
            """
            sql = sql.format(self.string.upper())
            value = []
            value_weather = []
            index = []
            p = 0
            weathering = 0
            print(self.ui.lineEdit_3.text())
            weathering = weather.Weather(self.ui.lineEdit_3.text())
            for i in range(len(s)):
                if s[i] == "@":
                    value.append(s[p:i])
                    p = i+1
            p = 0
            for i in range(len(weathering)):
                if weathering[i] == "@":
                    value_weather.append(weathering[p:i])
                    p = i+1
            if len(value) != 0:
                d = {"time": datetime.strftime(datetime.now(), "%H:%M"),
                    "ph": value[2], "turbidity": value[1], "tempa": value[3], "tempw": value[0], "long": value[6], "lat": value[5]}
                if self.cur.close != True:
                    self.cur.execute(sql, d)
                self.ui.label_23.setText(value[1])
                self.ui.label_24.setText(value[2])
                self.ui.label_25.setText(value[0])
                self.ui.label_28.setText(value[3])
                self.ui.label_30.setText(value[5])
                self.ui.label_31.setText(value[6])
                self.con.commit()
            else:
                self.ui.lineEdit_5.setText(s)
        try:
            if len(value_weather) != 0:
                self.ui.label_15.setText(value_weather[3] + " %")
                self.ui.label_16.setText(value_weather[2] + " m/s")
                self.ui.label_17.setText(value_weather[0])
                self.ui.label_11.setText(value_weather[4] + " mm. Hg. st.")
                if int(float(value_weather[1])) >= 0:
                    self.ui.label_20.setText(
                        "+" + str(int(float(value_weather[1]))) + " C°")
                else:
                    self.ui.label_20.setText(
                        str(int(float(value_weather[1]))) + " C°")
                if ("sun" in value_weather[0]) and (ind != 1):
                    ind = 1
                    self.ui.label.setPixmap(QPixmap("SSun.jpg"))
                elif ("rain" in value_weather[0]) and (ind != 2):
                    ind = 2
                    self.ui.label.setPixmap(QPixmap("Rain.jpg"))
                elif ("snow" in value_weather[0]) and (ind != 3):
                    ind = 3
                    self.ui.label.setPixmap(QPixmap("Snow.jpg"))
                elif ("cloud" in value_weather[0]) and (ind != 4):
                    ind = 4
                    self.ui.label.setPixmap(QPixmap("Cloud.jpg"))
                else:
                    self.ui.label.setPixmap(QPixmap("Cloud.jpg"))
        except:
            pass

    def close_event(self):
        self.hide()
        self.mythread.running = False
        self.mythread.wait(5000)
        event.accept()
        self.cur.close()
        self.con.close()


class WidgetResults(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = result.Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QTreeView.NoEditTriggers)
        self.ui.tableWidget.setRowCount(15)
        self.ui.dateTimeEdit.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.ui.pushButton.clicked.connect(self.result_command)

    def result_command(self):
        try:
            s = str(self.ui.dateTimeEdit.text())
            water_name = s[0:s.find(" ")] + "_" + s[(s.find(" ")+1):(len(s))] + "_" + str(
                self.ui.lineEdit_3.text()).replace(" ", "") + "_" + (str(self.ui.lineEdit_4.text())).replace(" ", "")
            self.con = sqlite3.connect("app.db")
            self.cur = self.con.cursor()
            self.cur.execute("SELECT * FROM '{}'".format(water_name.upper()))
            arr = self.cur.fetchall()
            for k in range(len(arr)):
                for i in range(7):
                    self.ui.tableWidget.setRowCount(
                        self.ui.tableWidget.rowCount() + 1)
                    self.ui.tableWidget.setItem(
                        k, i, QTableWidgetItem(arr[k][i]))
        except:
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_3.setText("не найдено")


class WidgetMap(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = map.Ui_Form()
        self.ui.setupUi(self)
        self.con = sqlite3.connect("app.db")
        self.cur = self.con.cursor()
        self.a = MapWidget()
        self.ui.gridLayout.addWidget(self.a)
        self.ui.pushButton.clicked.connect(self.map_command)
        self.ui.pushButton_2.clicked.connect(self.clean_map)
        self.ui.dateTimeEdit.setDisplayFormat("dd.MM.yyyy HH:mm")
        
    def map_command(self):
        try:
            s = str(self.ui.dateTimeEdit.text())
            water_name = s[0:s.find(" ")] + "_" + s[(s.find(" ")+1):(len(s))] +"_" + str(self.ui.lineEdit_3.text()).replace(" ", "") + "_" + (str(self.ui.lineEdit_4.text())).replace(" ", "")
            sql = "SELECT * FROM '{}'"
            self.cur.execute(sql.format(water_name.upper()))
            arr = self.cur.fetchall()
            pos = []
            positions = []
            for k in range(len(arr)):
                for i in range(5,7):
                    pos.append(float(arr[k][i]))
                positions.append((pos[1],pos[0]))
                pos = [] 
            print(positions)
            self.a.place_marks(positions)

        except:
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_3.setText("Не найдено")

    def clean_map(self):
        try:
            for i in reversed(range(self.ui.gridLayout.count())): 
                self.ui.gridLayout.itemAt(i).widget().setParent(None)
            self.a = MapWidget()
            self.ui.gridLayout.addWidget(self.a)
            self.cur.close()
            self.con.close()
        except:
            pass   

class WidgetInformation(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = information.Ui_Form()
        self.ui.setupUi(self)


indicator = 0
port = 0
ind = 1