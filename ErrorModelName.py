from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon

import CSS


class Ui_MainWindow(QObject):
    #set up error page for wrong model name selected
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(231, 77)
        MainWindow.setStyleSheet(CSS.BackgroundCSS)
        MainWindow.setWindowIcon(QIcon('ErrorIcon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ErrorText = QtWidgets.QLabel(self.centralwidget)
        self.ErrorText.setGeometry(QtCore.QRect(55, 20, 161, 16))
        self.ErrorText.setObjectName("ErrorText")

        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(140, 40, 75, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(CSS.QPushButtonCSS)
        self.CloseButton.clicked.connect(self.close)

        self.ErrorIcon = QtWidgets.QLabel(self.centralwidget)
        self.ErrorIcon.setGeometry(QtCore.QRect(0, 10, 51, 41))
        self.ErrorIcon.setStyleSheet(CSS.ErrorIconCSS)
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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
