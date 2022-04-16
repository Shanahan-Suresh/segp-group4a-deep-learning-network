from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon

import CSS


class Ui_MainWindow(QObject):
    def setupUi(self, Form):
        Form.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Form.setObjectName("Form")
        Form.setFixedSize(240, 83)
        Form.setWindowIcon(QIcon('CautionIcon.png'))

        self.ErrorMessage = QtWidgets.QLabel(Form)
        self.ErrorMessage.setGeometry(QtCore.QRect(10, 20, 221, 16))
        self.ErrorMessage.setObjectName("ErrorMessage")

        self.CloseButton = QtWidgets.QPushButton(Form)
        self.CloseButton.setGeometry(QtCore.QRect(150, 50, 75, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(CSS.QPushButtonCSS)
        self.CloseButton.clicked.connect(self.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Warning!"))
        self.ErrorMessage.setText(_translate("Form", "Please import the dataset and images folder!"))
        self.CloseButton.setText(_translate("Form", "Close"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # ++++
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(CSS.BackgroundCSS)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
