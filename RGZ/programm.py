import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from uis.interface import Ui_MainWindow
from RGZ.deter import *
import numpy as np

import os


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_Button)
        self.pushButton_2.clicked.connect(self.file_insert)
        self.data = []

    def file_insert(self):
        user_path = os.environ['USERPROFILE']
        user_path = user_path.replace("\\", "/")
        f = QFile('data.txt')
        if not f.open(QIODevice.Append | QIODevice.Text):
            QMessageBox.information(self, "Unable to open file", f.errorString())
            return

        out = QTextStream(f)
        for i, k in zip(self.data, range(len(self.data))):
            out << "x{} = ".format(k) << round(i, 4) << '\n'
        out << "\n"

    def push_Button(self):
        matrix = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

        vector = [0, 0, 0, 0]

        matrix[0][0] = (int(self.lineEdit.text()))
        matrix[0][1] = (int(self.lineEdit_2.text()))
        matrix[0][2] = (int(self.lineEdit_3.text()))
        matrix[0][3] = (int(self.lineEdit_4.text()))

        vector[0] = (int(self.lineEdit_5.text()))

        matrix[1][0] = (int(self.lineEdit_6.text()))
        matrix[1][1] = (int(self.lineEdit_7.text()))
        matrix[1][2] = (int(self.lineEdit_9.text()))
        matrix[1][3] = (int(self.lineEdit_8.text()))

        vector[1] = (int(self.lineEdit_10.text()))

        matrix[2][0] = (int(self.lineEdit_12.text()))
        matrix[2][1] = (int(self.lineEdit_13.text()))
        matrix[2][2] = (int(self.lineEdit_11.text()))
        matrix[2][3] = (int(self.lineEdit_14.text()))

        vector[2] = (int(self.lineEdit_15.text()))

        matrix[3][0] = (int(self.lineEdit_17.text()))
        matrix[3][1] = (int(self.lineEdit_18.text()))
        matrix[3][2] = (int(self.lineEdit_16.text()))
        matrix[3][3] = (int(self.lineEdit_19.text()))

        vector[3] = (int(self.lineEdit_20.text()))

        copy_matrix = []
        copy_vector = []

        for i in range(0, len(matrix)):  # We determine the number of equations, delete unnecessary lines
            if sum(matrix[i]) != 0:
                copy_matrix.append(matrix[i])
                copy_vector.append(vector[i])

        if len(copy_matrix) == 3:  # We reduce the matrix to a square form for the correct calculation of the roots
            for i in copy_matrix:
                del i[3]
        elif len(copy_matrix) == 2:
            for i in copy_matrix:
                del i[3]
                del i[2]

        del matrix  # free memory from unnecessary data
        del vector

        result = []

        if det(copy_matrix) == 0:  # Matrix determinant
            self.label_22.setText("The determinant is 0, the solution is not possible")


        else:
            result = np.linalg.solve(copy_matrix, copy_vector)

            for i in result:
                self.TextEdit_21.append("{}".format(round(i, 4)))
                self.data.append(i)


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
