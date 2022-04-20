from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
import setup


class Ui_MainWindow(QObject):
    # Show the wrong file imported pop up.
    def setupUi(self, MainWindow):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(260, 115)
        MainWindow.setStyleSheet(setup.BackgroundCSS)
        MainWindow.setWindowIcon(QIcon('Icons/ErrorIcon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ErrorIcon = QtWidgets.QLabel(self.centralwidget)
        self.ErrorIcon.setGeometry(QtCore.QRect(0, 10, 51, 41))
        self.ErrorIcon.setStyleSheet(setup.ErrorIconCSS)
        self.ErrorIcon.setObjectName("ErrorIcon")

        self.problem2 = QtWidgets.QLabel(self.centralwidget)
        self.problem2.setGeometry(QtCore.QRect(50, 60, 211, 16))
        self.problem2.setObjectName("problem2")
        self.problem1 = QtWidgets.QLabel(self.centralwidget)
        self.problem1.setGeometry(QtCore.QRect(50, 40, 211, 16))
        self.problem1.setObjectName("problem1")
        self.ErrorMessage = QtWidgets.QLabel(self.centralwidget)
        self.ErrorMessage.setGeometry(QtCore.QRect(50, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMessage.setFont(font)
        self.ErrorMessage.setObjectName("ErrorMessage")

        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(setup.QPushButtonCSS)
        self.CloseButton.clicked.connect(self.close)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Error!"))
        self.ErrorMessage.setText(_translate("MainWindow", "Following problem(s):"))
        self.CloseButton.setText(_translate("MainWindow", "Close"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.UpdateError()

    # Update error message.
    def UpdateError(self):
        file = open("Temp files/CorrectImportFilesRecieved.txt", "r")
        CorrectDataSet = file.readline().strip()
        CorrectImageFolder = file.readline().strip()
        print(CorrectDataSet)
        print(CorrectImageFolder)
        file.close()

        if CorrectDataSet == "0" and CorrectImageFolder == "0":
            self.problem1.setText("-Could not load data from given excel file!")
            self.problem2.setText("-Folder doesn\'t contain any bmt files!")
        else:
            if CorrectDataSet == "0" and CorrectImageFolder == "1":
                self.problem1.setText("-Could not load data from given excel file!")

            if CorrectDataSet == "1" and CorrectImageFolder == "0":
                self.problem1.setText("-Folder doesn\'t contain any bmt files!")
            self.problem2.hide()
