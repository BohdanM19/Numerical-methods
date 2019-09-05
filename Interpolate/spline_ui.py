# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spline_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

matplotlib.use('QT5Agg')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 669)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plot_widget = MplWidget(self.centralwidget)
        self.plot_widget.setGeometry(QtCore.QRect(20, 0, 921, 391))
        self.plot_widget.setObjectName("plot_widget")
        self.spline_button = QtWidgets.QPushButton(self.centralwidget)
        self.spline_button.setGeometry(QtCore.QRect(430, 430, 161, 41))
        self.spline_button.setObjectName("spline_button")
        self.y_array = QtWidgets.QLineEdit(self.centralwidget)
        self.y_array.setGeometry(QtCore.QRect(10, 520, 401, 41))
        self.y_array.setObjectName("y_array")
        self.x_label = QtWidgets.QLabel(self.centralwidget)
        self.x_label.setGeometry(QtCore.QRect(10, 410, 111, 16))
        self.x_label.setObjectName("x_label")
        self.y_label = QtWidgets.QLabel(self.centralwidget)
        self.y_label.setGeometry(QtCore.QRect(10, 500, 111, 16))
        self.y_label.setObjectName("y_label")
        self.x_array = QtWidgets.QLineEdit(self.centralwidget)
        self.x_array.setGeometry(QtCore.QRect(10, 430, 401, 41))
        self.x_array.setObjectName("x_array")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(660, 410, 141, 211))
        self.textEdit.setObjectName("textEdit")
        self.writeDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.writeDataButton.setGeometry(QtCore.QRect(830, 440, 101, 23))
        self.writeDataButton.setObjectName("writeDataButton")
        self.readDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.readDataButton.setGeometry(QtCore.QRect(430, 490, 161, 41))
        self.readDataButton.setObjectName("readDataButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spline_button.setText(_translate("MainWindow", "Сплайн!"))
        self.x_label.setText(_translate("MainWindow", "Строка для ввода X"))
        self.y_label.setText(_translate("MainWindow", "Строка для ввода Y"))
        self.writeDataButton.setText(_translate("MainWindow", "Записать в файл"))
        self.readDataButton.setText(_translate("MainWindow", "Исходные данные из файла"))


class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas()  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
