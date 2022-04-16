from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon

import CSS


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(304, 101)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ChangingText = QtWidgets.QLabel(self.centralwidget)
        self.ChangingText.setGeometry(QtCore.QRect(70, 10, 231, 16))
        self.ChangingText.setObjectName("ChangingText")

        self.NoButton = QtWidgets.QPushButton(self.centralwidget)
        self.NoButton.setGeometry(QtCore.QRect(220, 70, 75, 23))
        self.NoButton.setObjectName("NoButton")

        self.Icon = QtWidgets.QLabel(self.centralwidget)
        self.Icon.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.Icon.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Icon.setText("")
        self.Icon.setObjectName("Icon")

        self.FixedText = QtWidgets.QLabel(self.centralwidget)
        self.FixedText.setGeometry(QtCore.QRect(70, 30, 131, 16))
        self.FixedText.setObjectName("FixedText")

        self.YesButton = QtWidgets.QPushButton(self.centralwidget)
        self.YesButton.setGeometry(QtCore.QRect(140, 70, 75, 23))
        self.YesButton.setObjectName("YesButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Replace File"))
        self.NoButton.setText(_translate("MainWindow", "No"))
        self.FixedText.setText(_translate("MainWindow", "Do you want to replace it?"))
        self.YesButton.setText(_translate("MainWindow", "Yes"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(CSS.BackgroundCSS)
        self.YesButton.setStyleSheet(CSS.QPushButtonCSS)
        self.NoButton.setStyleSheet(CSS.QPushButtonCSS)
        self.Icon.setStyleSheet(CSS.CautionIconCSS)
        self.setWindowIcon(QIcon('Icons/CautionIcon.png'))

        file=open("Temp files/ModelName.txt","r")
        ModelName=file.read()
        file.close()
        self.ChangingText.setText(ModelName+".file already exists.")
        self.NoButton.clicked.connect(self.close)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())

