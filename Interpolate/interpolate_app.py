import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Interpolate.spline_ui import Ui_MainWindow
from RGZ.deter import *
import numpy as np
from scipy import interpolate
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.spline_button.clicked.connect(self.plot_data)
        self.writeDataButton.clicked.connect(self.file_insert)
        self.readDataButton.clicked.connect(self.file_output)
        self.x_global = []
        self.y_global = []

    def file_output(self):  # Read data from file

        with open("read_data.txt", 'r') as file:
            x_array = file.readline()
            y_array = file.readline()

            x_array = x_array.split(" ")
            y_array = y_array.split(" ")
            self.draw(x_array, y_array)

    def file_insert(self):  # Запись в файл

        f = QFile('interpolate.txt')
        if not f.open(QIODevice.Append | QIODevice.Text):
            QMessageBox.information(self, "Unable to open file", f.errorString())
            return

        out = QTextStream(f)
        for i in range(0, len(self.x_global)):
            out << "{} {}".format(self.x_global[i], self.y_global[i]) << round(i, 4)
            out << '\n'
        out << "\n"

    def plot_data(self):

        x_array = (self.x_array.text())
        y_array = (self.y_array.text())

        x_array = x_array.split(" ")
        y_array = y_array.split(" ")

        if len(x_array) != len(y_array):
            self.x_label.setText("Invalid input!")
            return
        self.draw(x_array, y_array)

    def draw(self, x_array, y_array):
        for i in range(0, len(x_array)):
            x_array[i] = int(x_array[i])
            y_array[i] = float(y_array[i])

        f2 = interpolate.interp1d(x_array, y_array, kind='cubic')
        xnew = np.linspace(0, len(x_array) - 1, num=100, endpoint=True)
        self.plot_widget.canvas.ax.plot(xnew, f2(xnew))
        self.plot_widget.canvas.draw()

        ynew = f2(xnew)
        for i in range(0, len(xnew)):
            self.textEdit.append("{}  {}".format(round(xnew[i], 4), round(ynew[i], 4)))

        self.x_global = copy.deepcopy(xnew)
        self.y_global = copy.deepcopy(ynew)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
