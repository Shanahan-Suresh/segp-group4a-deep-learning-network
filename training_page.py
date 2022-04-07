from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from matplotlib import pyplot as plt

import CSS
from train_neural_network import main as train,get_graph,save_model


class MainBackgroundThread(QThread):
    def __init__(self, ImportDataPath, ImportImagesPath, Epoch,TrainingMode, TrainingRatio, LearningRate,Momentum,preview_image,original_image,progress_bar,graph_widget,epoch_loss_widget,total_loss_widget):
        QThread.__init__(self)
        self.ImportDataPath, self.ImportImagesPath,self.Epoch,self.TrainingMode, self.TrainingRatio, self.LearningRate,self.Momentum,self.PreviewImage,self.OriginalImage,self.ProgressBar,self.Graph,self.Epoch_loss,self.Total_loss = ImportDataPath, ImportImagesPath,Epoch,TrainingMode,TrainingRatio,LearningRate,Momentum,preview_image,original_image,progress_bar,graph_widget,epoch_loss_widget,total_loss_widget
    def run(self):
        train(self.ImportDataPath, self.ImportImagesPath,self.Epoch,self.TrainingMode,self.TrainingRatio,self.LearningRate,self.Momentum,self.PreviewImage,self.OriginalImage,self.ProgressBar,self.Epoch_loss,self.Total_loss)
        x,training_loss_arr,validation_loss_arr = get_graph()
        plt.plot(x, training_loss_arr, color='r', label='training loss')
        plt.plot(x, validation_loss_arr, color='g', label='validation loss')
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.title("Training Loss and Validation Loss")
        plt.legend()
        plt.savefig("loss_graph")
        self.Graph.setStyleSheet("image: url(loss_graph.png);border :1px solid black;")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 576)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EpochText = QtWidgets.QLabel(self.centralwidget)
        self.EpochText.setGeometry(QtCore.QRect(510, 190, 47, 13))
        self.EpochText.setObjectName("EpochText")
        self.TrainModeText = QtWidgets.QLabel(self.centralwidget)
        self.TrainModeText.setGeometry(QtCore.QRect(480, 220, 81, 16))
        self.TrainModeText.setObjectName("TrainModeText")
        self.TrainingRatioText = QtWidgets.QLabel(self.centralwidget)
        self.TrainingRatioText.setGeometry(QtCore.QRect(480, 260, 71, 16))
        self.TrainingRatioText.setObjectName("TrainingRatioText")
        self.Epoch = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Epoch.setGeometry(QtCore.QRect(560, 180, 62, 22))
        self.Epoch.setObjectName("Epoch")
        self.TrainingMode = QtWidgets.QComboBox(self.centralwidget)
        self.TrainingMode.setGeometry(QtCore.QRect(560, 220, 69, 22))
        self.TrainingMode.setObjectName("TrainingMode")
        self.TrainingMode.addItem("")
        self.TrainingMode.addItem("")
        self.TrainingRatio = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.TrainingRatio.setGeometry(QtCore.QRect(560, 260, 62, 22))
        self.TrainingRatio.setObjectName("TrainingRatio")
        self.Momentum = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Momentum.setGeometry(QtCore.QRect(740, 220, 62, 22))
        self.Momentum.setObjectName("Momentum")
        self.LearningRateText = QtWidgets.QLabel(self.centralwidget)
        self.LearningRateText.setGeometry(QtCore.QRect(660, 190, 71, 16))
        self.LearningRateText.setObjectName("LearningRateText")
        self.MomentumText = QtWidgets.QLabel(self.centralwidget)
        self.MomentumText.setGeometry(QtCore.QRect(670, 220, 61, 16))
        self.MomentumText.setObjectName("MomentumText")
        self.LearningRate = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.LearningRate.setGeometry(QtCore.QRect(740, 190, 62, 22))
        self.LearningRate.setObjectName("LearningRate")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(633, 170, 20, 121))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.AdvancedOptionsText = QtWidgets.QLabel(self.centralwidget)
        self.AdvancedOptionsText.setGeometry(QtCore.QRect(680, 170, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AdvancedOptionsText.setFont(font)
        self.AdvancedOptionsText.setObjectName("AdvancedOptionsText")
        self.ImportDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportDataButton.setGeometry(QtCore.QRect(460, 30, 91, 23))
        self.ImportDataButton.setStyleSheet("QPushButton {\n"
                                            "color: #000;\n"
                                            "border: 2px solid #555;\n"
                                            "border-radius: 20px;\n"
                                            "border-style: outset;\n"
                                            "background: qradialgradient(\n"
                                            "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                            "radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                            ");\n"
                                            "padding: 1px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background: qradialgradient(\n"
                                            "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                            "radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                            ");\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "border-style: inset;\n"
                                            "background: qradialgradient(\n"
                                            "cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                            "radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                            ");\n"
                                            "}")
        self.ImportDataButton.setObjectName("ImportDataButton")
        self.ImportImagesButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportImagesButton.setGeometry(QtCore.QRect(460, 60, 91, 23))
        self.ImportImagesButton.setStyleSheet("QPushButton {\n"
                                              "color: #000;\n"
                                              "border: 2px solid #555;\n"
                                              "border-radius: 20px;\n"
                                              "border-style: outset;\n"
                                              "background: qradialgradient(\n"
                                              "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                              "radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                              ");\n"
                                              "padding: 1px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background: qradialgradient(\n"
                                              "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                              "radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                              ");\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "border-style: inset;\n"
                                              "background: qradialgradient(\n"
                                              "cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                              "radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                              ");\n"
                                              "}")
        self.ImportImagesButton.setObjectName("ImportImagesButton")
        self.ImportDataPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ImportDataPath.setGeometry(QtCore.QRect(560, 30, 281, 20))
        self.ImportDataPath.setText("")
        self.ImportDataPath.setReadOnly(True)
        self.ImportDataPath.setObjectName("ImportDataPath")
        self.ImportImagesPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ImportImagesPath.setGeometry(QtCore.QRect(560, 60, 281, 20))
        self.ImportImagesPath.setText("")
        self.ImportImagesPath.setReadOnly(True)
        self.ImportImagesPath.setObjectName("ImportImagesPath")
        self.OriginalIMage = QtWidgets.QLabel(self.centralwidget)
        self.OriginalIMage.setGeometry(QtCore.QRect(30, 50, 191, 161))
        self.OriginalIMage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.OriginalIMage.setText("")
        self.OriginalIMage.setObjectName("OriginalIMage")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 270, 441, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.ConfigureModelText = QtWidgets.QLabel(self.centralwidget)
        self.ConfigureModelText.setGeometry(QtCore.QRect(580, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ConfigureModelText.setFont(font)
        self.ConfigureModelText.setObjectName("ConfigureModelText")
        self.NewImage = QtWidgets.QLabel(self.centralwidget)
        self.NewImage.setGeometry(QtCore.QRect(240, 50, 191, 161))
        self.NewImage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.NewImage.setText("")
        self.NewImage.setObjectName("NewImage")
        self.EpochLoss = QtWidgets.QLabel(self.centralwidget)
        self.EpochLoss.setGeometry(QtCore.QRect(30, 500, 191, 16))
        self.EpochLoss.setObjectName("EpochLoss")
        self.TotalTrainingLoss = QtWidgets.QLabel(self.centralwidget)
        self.TotalTrainingLoss.setGeometry(QtCore.QRect(30, 530, 191, 16))
        self.TotalTrainingLoss.setObjectName("TotalTrainingLoss")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(30, 230, 41, 31))
        self.StartButton.setObjectName("StartButton")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(80, 230, 41, 31))
        self.StopButton.setObjectName("StopButton")
        self.SaveModelButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveModelButton.setGeometry(QtCore.QRect(500, 500, 100, 31))
        self.SaveModelButton.setObjectName("SaveModel")
        self.ModelName = QtWidgets.QLineEdit(self.centralwidget)
        self.ModelName.setGeometry(QtCore.QRect(560, 90, 281, 20))
        self.ModelName.setObjectName("ModelName")
        self.ModelNameText = QtWidgets.QLabel(self.centralwidget)
        self.ModelNameText.setGeometry(QtCore.QRect(490, 90, 61, 16))
        self.ModelNameText.setObjectName("ModelNameText")
        self.Graph = QtWidgets.QLabel(self.centralwidget)
        self.Graph.setGeometry(QtCore.QRect(30, 310, 191, 161))
        self.Graph.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Graph.setText("")
        self.Graph.setObjectName("Graph")
        MainWindow.setCentralWidget(self.centralwidget)

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
        self.LearningRateText.setText(_translate("MainWindow", "Learning rate:"))
        self.MomentumText.setText(_translate("MainWindow", "Momentum:"))
        self.AdvancedOptionsText.setText(_translate("MainWindow", "Advanced Options"))
        self.ImportDataButton.setText(_translate("MainWindow", "Import Data"))
        self.ImportImagesButton.setText(_translate("MainWindow", "Import Images"))
        self.ConfigureModelText.setText(_translate("MainWindow", "Configure Model"))
        self.EpochLoss.setText(_translate("MainWindow", "Current epoch loss :"))
        self.TotalTrainingLoss.setText(_translate("MainWindow", "Total training loss:"))
        self.StartButton.setText(_translate("MainWindow", "PushButton"))
        self.StopButton.setText(_translate("MainWindow", "PushButton"))
        self.ModelNameText.setText(_translate("MainWindow", "Model Name:"))
        self.SaveModelButton.setText(_translate("MainWindow", "Save Model"))

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # ++++
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ImportDataButton.clicked.connect(self.ImportData)
        self.ImportImagesButton.clicked.connect(self.ImportImages)
        self.StartButton.clicked.connect(self.StartTraining)
        self.SaveModelButton.clicked.connect(self.SaveModel)


    def ImportData(self):
        filename = QFileDialog.getOpenFileName(None, "Open Model",
                                               "", " Excel File *.xlsx")
        path = filename[0]
        self.ImportDataPath.setText(path)

    def ImportImages(self):
        filename = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        path = filename
        self.ImportImagesPath.setText(path)

    def StartTraining(self):
        self.worker = MainBackgroundThread(self.ImportDataPath.text(), self.ImportImagesPath.text(), self.Epoch.text(),
                                           self.TrainingMode.currentText(), self.TrainingRatio.text(), self.LearningRate.text(),
                                           self.Momentum.text(),self.NewImage,self.OriginalIMage,self.progressBar,self.Graph,self.EpochLoss,self.TotalTrainingLoss)

        print("hi")
        self.worker.start()
    def SaveModel(self):
        save_model(self.ModelName.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
