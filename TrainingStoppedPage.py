from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
import CSS


class Ui_MainWindow(QObject):
    # Set up training stopped page.
    def setupUi(self, MainWindow):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(261, 77)
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.MessageText = QtWidgets.QLabel(self.centralwidget)
        self.MessageText.setGeometry(QtCore.QRect(70, 20, 161, 16))
        self.MessageText.setObjectName("MessageText")

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(180, 50, 75, 23))
        self.closeButton.setObjectName("closeButton")

        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.icon.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.icon.setText("")
        self.icon.setObjectName("icon")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stop training"))
        self.closeButton.setText(_translate("MainWindow", "Close"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(CSS.BackgroundCSS)
        self.setWindowIcon(QIcon('Icons/TrainingIcon.png'))

        self.icon.setStyleSheet(CSS.CautionIconCSS)
        self.MessageText.setText("Training has been stopped.")

        self.closeButton.setStyleSheet(CSS.QPushButtonCSS)
        self.closeButton.clicked.connect(self.close)