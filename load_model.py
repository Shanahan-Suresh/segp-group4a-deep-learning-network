import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog

import CSS


def Load():
    filename = QFileDialog.getOpenFileName(None, "Open Model",
                                           "", "Trained Model (*);")
    path = filename[0]
    print(path)
    if not os.stat('Path.txt').st_size == 0:
        file = open('Path.txt', 'w')
        file.write(path)
        file.close()
        if path=='':
            file = open('Path.txt', 'w')
            file.write('PreInstalledModel')
            file.close()


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        self.setWindowIcon(QIcon('SelectModelIcon.png'))
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SelectModel = QtWidgets.QComboBox(self.centralwidget)
        self.SelectModel.setGeometry(QtCore.QRect(70, 10, 121, 22))
        self.SelectModel.setObjectName("comboBox")
        self.SelectModel.addItem("")
        self.SelectModel.addItem("")
        self.SelectModel.setStyleSheet(CSS.QComboBoxCSS)
        self.ModelLabel = QtWidgets.QLabel(self.centralwidget)
        self.ModelLabel.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.ModelLabel.setObjectName("ModelLabel")
        self.LoadModel = QtWidgets.QPushButton(self.centralwidget)
        self.LoadModel.setGeometry(QtCore.QRect(90, 50, 51, 41))
        self.LoadModel.setStyleSheet(CSS.LoadIconCSS)
        self.LoadModel.setText("")
        self.LoadModel.setObjectName("pushButton_2")
        self.LoadModelLabel = QtWidgets.QLabel(self.centralwidget)
        self.LoadModelLabel.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.LoadModelLabel.setObjectName("LoadModelLabel")
        self.ApplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.ApplyButton.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.ApplyButton.setObjectName("pushButton")
        self.ApplyButton.setStyleSheet(CSS.QPushButtonCSS)
        self.LoadModelVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Select Model"))
        self.SelectModel.setItemText(0, _translate("MainWindow", "Pre installed model"))
        self.SelectModel.setItemText(1, _translate("MainWindow", "Load model"))
        self.ModelLabel.setText(_translate("MainWindow", "Model: "))
        self.LoadModelLabel.setText(_translate("MainWindow", "Load model:"))
        self.ApplyButton.setText(_translate("MainWindow", "Apply"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(239, 138)
        self.setStyleSheet(CSS.BackgroundCSS)
        self.SelectModel.activated.connect(self.updateMainWindow)
        self.LoadModel.clicked.connect(Load)
        self.ApplyButton.clicked.connect(self.Close)

    def Close(self):
        if self.SelectModel.currentIndex() == 0:
            file = open('Path.txt', 'w')
            file.write('PreInstalledModel')
            file.close()
        self.close()

    def updateMainWindow(self):
        if self.SelectModel.currentIndex() == 1:
            self.LoadModelVisible(True)
        else:
            self.LoadModelVisible(False)

    def LoadModelVisible(self, visible):
        self.LoadModelLabel.setVisible(visible)
        self.LoadModel.setVisible(visible)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
