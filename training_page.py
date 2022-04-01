from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog
from train_neural_network import main as train


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 235)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EpochText = QtWidgets.QLabel(self.centralwidget)
        self.EpochText.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.EpochText.setObjectName("EpochText")
        self.TrainModeText = QtWidgets.QLabel(self.centralwidget)
        self.TrainModeText.setGeometry(QtCore.QRect(30, 110, 81, 16))
        self.TrainModeText.setObjectName("TrainModeText")
        self.TrainingRatioText = QtWidgets.QLabel(self.centralwidget)
        self.TrainingRatioText.setGeometry(QtCore.QRect(30, 150, 71, 16))
        self.TrainingRatioText.setObjectName("TrainingRatioText")
        self.Epoch = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Epoch.setGeometry(QtCore.QRect(90, 80, 62, 22))
        self.Epoch.setObjectName("Epoch")
        self.TrainingMode = QtWidgets.QComboBox(self.centralwidget)
        self.TrainingMode.setGeometry(QtCore.QRect(110, 110, 69, 22))
        self.TrainingMode.setObjectName("TrainingMode")
        self.TrainingMode.addItem("")
        self.TrainingMode.addItem("")
        self.TrainingRatio = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.TrainingRatio.setGeometry(QtCore.QRect(110, 150, 62, 22))
        self.TrainingRatio.setObjectName("TrainingRatio")
        self.StartTrainingButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartTrainingButton.setGeometry(QtCore.QRect(20, 190, 101, 23))
        self.StartTrainingButton.setObjectName("StartTraininButton")
        self.Momentum = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Momentum.setGeometry(QtCore.QRect(290, 120, 62, 22))
        self.Momentum.setObjectName("Momentum")
        self.LearningRateText = QtWidgets.QLabel(self.centralwidget)
        self.LearningRateText.setGeometry(QtCore.QRect(210, 90, 71, 16))
        self.LearningRateText.setObjectName("LearningRateText")
        self.MomentumText = QtWidgets.QLabel(self.centralwidget)
        self.MomentumText.setGeometry(QtCore.QRect(220, 120, 61, 16))
        self.MomentumText.setObjectName("MomentumText")
        self.LearningRate = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.LearningRate.setGeometry(QtCore.QRect(290, 90, 62, 22))
        self.LearningRate.setObjectName("LearningRate")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(183, 70, 20, 151))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.AdvancedOptionsText = QtWidgets.QLabel(self.centralwidget)
        self.AdvancedOptionsText.setGeometry(QtCore.QRect(230, 70, 101, 16))
        self.AdvancedOptionsText.setObjectName("AdvancedOptionsText")
        self.ImportDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportDataButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.ImportDataButton.setObjectName("ImportDataButton")
        self.ImportImagesButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportImagesButton.setGeometry(QtCore.QRect(10, 40, 91, 23))
        self.ImportImagesButton.setObjectName("ImportImagesButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.ImportDataPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ImportDataPath.setGeometry(QtCore.QRect(110, 10, 231, 20))
        self.ImportDataPath.setText("")
        self.ImportDataPath.setReadOnly(True)
        self.ImportDataPath.setObjectName("ImportDataPath")
        self.ImportImagesPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ImportImagesPath.setGeometry(QtCore.QRect(110, 40, 231, 20))
        self.ImportImagesPath.setText("")
        self.ImportImagesPath.setReadOnly(True)
        self.ImportImagesPath.setObjectName("ImportImagesPath")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EpochText.setText(_translate("MainWindow", "Epoch: "))
        self.TrainModeText.setText(_translate("MainWindow", "Training mode:"))
        self.TrainingRatioText.setText(_translate("MainWindow", "Training ratio: "))
        self.TrainingMode.setItemText(0, _translate("MainWindow", "CPU"))
        self.TrainingMode.setItemText(1, _translate("MainWindow", "GPU"))
        self.StartTrainingButton.setText(_translate("MainWindow", "Start training"))
        self.LearningRateText.setText(_translate("MainWindow", "Learning rate:"))
        self.MomentumText.setText(_translate("MainWindow", "Momentum:"))
        self.AdvancedOptionsText.setText(_translate("MainWindow", "Advanced Options"))
        self.ImportDataButton.setText(_translate("MainWindow", "Import Data"))
        self.ImportImagesButton.setText(_translate("MainWindow", "Import Images"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # ++++

    data_path = ""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ImportDataButton.clicked.connect(self.ImportData)
        self.ImportImagesButton.clicked.connect(self.ImportImages)
        self.StartTrainingButton.clicked.connect(self.StartTraining)

    def ImportData(self):
        filename = QFileDialog.getOpenFileName(None, "Open Model",
                                               "", " Excel File *.xlsx")
        data_path = filename[0]
        self.ImportDataPath.setText(data_path)

    def ImportImages(self):
        filename = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        image_path = filename
        self.ImportImagesPath.setText(image_path)


    def StartTraining(self):
        train(self.ImportDataPath.text(),self.ImportImagesPath.text(),self.Epoch.text(),self.TrainingMode.currentText(),self.TrainingRatio.text(),self.LearningRate.text(),self.Momentum.text())





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
