from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon

import CSS
import load_model


class Ui_MainWindow(QObject):
    # Set up error pop up UI page.
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(475, 97)
        MainWindow.setStyleSheet(CSS.BackgroundCSS)
        MainWindow.setWindowIcon(QIcon('Icons/ErrorIcon.png'))

        self.ErrorIcon = QtWidgets.QLabel(MainWindow)
        self.ErrorIcon.setGeometry(QtCore.QRect(5, 15, 51, 41))
        self.ErrorIcon.setStyleSheet(CSS.ErrorIconCSS)
        self.ErrorIcon.setObjectName("ErrorIcon")

        self.CloseButton = QtWidgets.QPushButton(MainWindow)
        self.CloseButton.setGeometry(QtCore.QRect(370, 60, 75, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(CSS.QPushButtonCSS)

        self.LoadModelButton = QtWidgets.QPushButton(MainWindow)
        self.LoadModelButton.setGeometry(QtCore.QRect(270, 60, 90, 23))
        self.LoadModelButton.setObjectName("LoadModelButton")
        self.LoadModelButton.setStyleSheet(CSS.QPushButtonCSS)
        self.LoadModelButton.clicked.connect(self.LoadModel)

        self.AlertMessage = QtWidgets.QLabel(MainWindow)
        self.AlertMessage.setGeometry(QtCore.QRect(60, 10, 401, 51))
        self.AlertMessage.setObjectName("AlertMessage")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Error!"))
        self.CloseButton.setText(_translate("Form", "Close"))
        self.LoadModelButton.setText(_translate("Form", "Load Model"))
        self.AlertMessage.setText(
            _translate("Form", "Model could not be loaded! Please verify that the file is a trained neural network."))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CloseButton.clicked.connect(self.close)

    # method to open Load model screen
    def LoadModel(self):
        self.close()
        self.window = QtWidgets.QMainWindow()
        self.window = load_model.MyWindow()
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
