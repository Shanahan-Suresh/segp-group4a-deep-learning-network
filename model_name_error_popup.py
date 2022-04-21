from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
import setup


class Ui_MainWindow(QObject):
    # Set up error page for wrong model name selected
    def setupUi(self, MainWindow):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(231, 77)
        MainWindow.setStyleSheet(setup.BackgroundCSS)
        MainWindow.setWindowIcon(QIcon('Icons/ErrorIcon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ErrorText = QtWidgets.QLabel(self.centralwidget)
        self.ErrorText.setGeometry(QtCore.QRect(55, 20, 161, 16))
        self.ErrorText.setObjectName("ErrorText")

        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(140, 40, 75, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(setup.QPushButtonCSS)
        self.CloseButton.clicked.connect(self.close)

        self.ErrorIcon = QtWidgets.QLabel(self.centralwidget)
        self.ErrorIcon.setGeometry(QtCore.QRect(0, 10, 51, 41))
        self.ErrorIcon.setStyleSheet(setup.ErrorIconCSS)
        self.ErrorIcon.setObjectName("ErrorIcon")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Error!"))
        self.ErrorText.setText(_translate("MainWindow", "Please enter a valid model name!"))
        self.CloseButton.setText(_translate("MainWindow", "Close"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
