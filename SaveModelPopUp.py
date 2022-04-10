from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject

import CSS
import load_model


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(241, 77)
        MainWindow.setStyleSheet(CSS.BackgroundCSS
                                 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.SaveAsText = QtWidgets.QLabel(self.centralwidget)
        self.SaveAsText.setGeometry(QtCore.QRect(80, 20, 161, 16))
        self.SaveAsText.setObjectName("SaveAsText")

        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(160, 50, 75, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(CSS.QPushButtonCSS)
        self.CloseButton.clicked.connect(self.close)

        self.HappyIcon = QtWidgets.QLabel(self.centralwidget)
        self.HappyIcon.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.HappyIcon.setStyleSheet(CSS.HappyIconCSS)
        self.HappyIcon.setText("")
        self.HappyIcon.setObjectName("HappyIcon")

        self.LoadModelButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadModelButton.setGeometry(QtCore.QRect(80, 50, 75, 23))
        self.LoadModelButton.setStyleSheet(CSS.QPushButtonCSS)
        self.LoadModelButton.setObjectName("LoadModelButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SaveAsText.setText(_translate("MainWindow", "Model saved as abc!"))
        self.CloseButton.setText(_translate("MainWindow", "Close"))
        self.LoadModelButton.setText(_translate("MainWindow", "Load Model"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # ++++
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoadModelName()
        self.LoadModelButton.clicked.connect(self.openLoadWindow)

    def LoadModelName(self):
        file=open("ModelName.txt","r")
        self.SaveAsText.setText("Model saved as " +file.read() + "!")
        file.close()

    def openLoadWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window = load_model.MyWindow()
        self.window.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
