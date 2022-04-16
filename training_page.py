import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from matplotlib import pyplot as plt
import CSS
import ErrorModelName
import ReplaceFileWindow
import SaveModelPopUp
import TrainingPageDataErrorPopUp
import TrainingStoppedPage
import WrongFileImportedError
from train_neural_network import main as train, get_graph, save_model
import extract_data as extract

#self.statusbar = QtWidgets.QStatusBar(MainWindow)
#self.statusbar.setObjectName("statusbar")
#MainWindow.setStatusBar(self.statusbar)

class MainBackgroundThread(QThread):
    file = open("Temp files/StopTrainingFlag.txt", "w")
    file.write("0")
    file.close()

    def __init__(self, ImportDataPath, ImportImagesPath, Epoch, TrainingMode, TrainingRatio, LearningRate, Momentum,
                 preview_image, original_image, progress_bar, graph_widget, epoch_loss_widget, total_loss_widget):
        QThread.__init__(self)
        self.ImportDataPath, self.ImportImagesPath, self.Epoch, self.TrainingMode, self.TrainingRatio, self.LearningRate, self.Momentum, self.PreviewImage, self.OriginalImage, self.ProgressBar, self.Graph, self.Epoch_loss, self.Total_loss = ImportDataPath, ImportImagesPath, Epoch, TrainingMode, TrainingRatio, LearningRate, Momentum, preview_image, original_image, progress_bar, graph_widget, epoch_loss_widget, total_loss_widget

    def run(self):
        train(self.ImportDataPath, self.ImportImagesPath, self.Epoch, self.TrainingMode, self.TrainingRatio,
              self.LearningRate, self.Momentum, self.PreviewImage, self.OriginalImage, self.ProgressBar,
              self.Epoch_loss, self.Total_loss)

        file = open("Temp files/StopTrainingFlag.txt", "r")
        if file.read() == "1":
            return
        file.close()

        plt.cla()
        x, training_loss_arr, validation_loss_arr = get_graph()
        plt.plot(x, training_loss_arr, color='r', label='training loss')
        plt.plot(x, validation_loss_arr, color='g', label='validation loss')
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.title("Training Loss and Validation Loss")
        plt.legend()
        plt.savefig("Temp files/loss_graph")
        self.Graph.setStyleSheet("image: url(Temp files/loss_graph.png);border :1px solid black;")


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(852, 539)
        MainWindow.setStyleSheet(CSS.BackgroundCSS)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.EpochText = QtWidgets.QLabel(self.centralwidget)
        self.EpochText.setGeometry(QtCore.QRect(70, 320, 47, 13))
        self.EpochText.setObjectName("EpochText")

        self.TrainModeText = QtWidgets.QLabel(self.centralwidget)
        self.TrainModeText.setGeometry(QtCore.QRect(40, 350, 81, 16))
        self.TrainModeText.setObjectName("TrainModeText")

        self.TrainingRatioText = QtWidgets.QLabel(self.centralwidget)
        self.TrainingRatioText.setGeometry(QtCore.QRect(40, 390, 71, 16))
        self.TrainingRatioText.setObjectName("TrainingRatioText")

        self.Epoch = QtWidgets.QSpinBox(self.centralwidget)
        self.Epoch.setGeometry(QtCore.QRect(120, 310, 62, 22))
        self.Epoch.setAccelerated(True)
        self.Epoch.setMinimum(2)
        self.Epoch.setValue(30)
        self.Epoch.setMaximum(3000)
        self.Epoch.setObjectName("Epoch")
        self.Epoch.setStyleSheet(CSS.QSpinBoxCSS)

        self.TrainingMode = QtWidgets.QComboBox(self.centralwidget)
        self.TrainingMode.setGeometry(QtCore.QRect(120, 350, 69, 22))
        self.TrainingMode.setObjectName("TrainingMode")
        self.TrainingMode.setStyleSheet(CSS.QComboBoxCSS)
        self.TrainingMode.addItem("")
        self.TrainingMode.addItem("")

        self.TrainingRatio = QtWidgets.QSpinBox(self.centralwidget)
        self.TrainingRatio.setGeometry(QtCore.QRect(120, 390, 62, 22))
        self.TrainingRatio.setAccelerated(True)
        self.TrainingRatio.setMinimum(2)
        self.TrainingRatio.setValue(90)
        self.TrainingRatio.setMaximum(95)
        self.TrainingRatio.setObjectName("TrainingRatio")
        self.TrainingRatio.setStyleSheet(CSS.QSpinBoxCSS)

        self.Momentum = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Momentum.setDecimals(4)
        self.Momentum.setAccelerated(True)
        self.Momentum.setSingleStep(0.0001)
        self.Momentum.setMinimum(0.5)
        self.Momentum.setValue(0.9)
        self.Momentum.setMaximum(0.99)
        self.Momentum.setGeometry(QtCore.QRect(320, 360, 62, 22))
        self.Momentum.setObjectName("Momentum")
        self.Momentum.setStyleSheet(CSS.QDoubleSpinBoxCSS)

        self.LearningRateText = QtWidgets.QLabel(self.centralwidget)
        self.LearningRateText.setGeometry(QtCore.QRect(240, 330, 71, 16))
        self.LearningRateText.setObjectName("LearningRateText")

        self.MomentumText = QtWidgets.QLabel(self.centralwidget)
        self.MomentumText.setGeometry(QtCore.QRect(250, 360, 61, 16))
        self.MomentumText.setObjectName("MomentumText")

        self.LearningRate = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.LearningRate.setDecimals(4)
        self.LearningRate.setAccelerated(True)
        self.LearningRate.setSingleStep(0.0001)
        self.LearningRate.setMinimum(0.0001)
        self.LearningRate.setValue(0.009)
        self.LearningRate.setMaximum(0.9999)
        self.LearningRate.setGeometry(QtCore.QRect(320, 330, 62, 22))
        self.LearningRate.setObjectName("LearningRate")
        self.LearningRate.setStyleSheet(CSS.QDoubleSpinBoxCSS)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(213, 300, 20, 121))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.AdvancedOptionsText = QtWidgets.QLabel(self.centralwidget)
        self.AdvancedOptionsText.setGeometry(QtCore.QRect(260, 300, 111, 16))
        self.AdvancedOptionsText.setObjectName("AdvancedOptionsText")

        self.ImportDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportDataButton.setGeometry(QtCore.QRect(460, 50, 91, 23))
        self.ImportDataButton.setStyleSheet(CSS.QPushButtonCSS)
        self.ImportDataButton.setObjectName("ImportDataButton")

        self.ImportImagesButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportImagesButton.setGeometry(QtCore.QRect(460, 80, 91, 23))
        self.ImportImagesButton.setStyleSheet(CSS.QPushButtonCSS)
        self.ImportImagesButton.setObjectName("ImportImagesButton")

        self.ImportDataPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ImportDataPath.setGeometry(QtCore.QRect(560, 50, 281, 20))
        self.ImportDataPath.setText("")
        self.ImportDataPath.setReadOnly(True)
        self.ImportDataPath.setObjectName("ImportDataPath")
        self.ImportDataPath.setStyleSheet(CSS.QLineEditCSS)

        self.ImportImagesPath = QtWidgets.QLineEdit(self.centralwidget)
        self.ImportImagesPath.setGeometry(QtCore.QRect(560, 80, 281, 20))
        self.ImportImagesPath.setText("")
        self.ImportImagesPath.setReadOnly(True)
        self.ImportImagesPath.setObjectName("ImportImagesPath")
        self.ImportImagesPath.setStyleSheet(CSS.QLineEditCSS)

        self.OriginalImage = QtWidgets.QLabel(self.centralwidget)
        self.OriginalImage.setGeometry(QtCore.QRect(20, 80, 160, 120))
        self.OriginalImage.setStyleSheet(CSS.DefaultPicturesCSS)
        self.OriginalImage.setText("")
        self.OriginalImage.setObjectName("OriginalImage")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(130, 470, 281, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")

        self.ConfigureModelText = QtWidgets.QLabel(self.centralwidget)
        self.ConfigureModelText.setGeometry(QtCore.QRect(180, 270, 161, 31))
        self.ConfigureModelText.setObjectName("ConfigureModelText")

        self.NewImage = QtWidgets.QLabel(self.centralwidget)
        self.NewImage.setGeometry(QtCore.QRect(230, 80, 160, 120))
        self.NewImage.setStyleSheet(CSS.PreviewImageCSS)
        self.NewImage.setText("")
        self.NewImage.setObjectName("NewImage")
        self.NewImage.setStyleSheet(CSS.DefaultPicturesCSS)

        self.EpochLoss = QtWidgets.QLabel(self.centralwidget)
        self.EpochLoss.setGeometry(QtCore.QRect(495, 390, 191, 16))
        self.EpochLoss.setObjectName("EpochLoss")

        self.TotalTrainingLoss = QtWidgets.QLabel(self.centralwidget)
        self.TotalTrainingLoss.setGeometry(QtCore.QRect(495, 420, 191, 16))
        self.TotalTrainingLoss.setObjectName("TotalTrainingLoss")

        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(30, 470, 41, 31))
        self.StartButton.setObjectName("StartButton")
        self.StartButton.setStyleSheet(CSS.StartButtonCSS)

        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(80, 470, 41, 31))
        self.StopButton.setObjectName("StopButton")
        self.StopButton.setStyleSheet(CSS.PauseButtonCSS)

        self.ModelName = QtWidgets.QLineEdit(self.centralwidget)
        self.ModelName.setMaxLength(50)
        self.ModelName.setGeometry(QtCore.QRect(110, 430, 281, 20))
        self.ModelName.setObjectName("ModelName")
        self.ModelName.setStyleSheet(CSS.QLineEditCSS)

        self.ModelNameText = QtWidgets.QLabel(self.centralwidget)
        self.ModelNameText.setGeometry(QtCore.QRect(40, 430, 61, 16))
        self.ModelNameText.setObjectName("ModelNameText")

        self.Graph = QtWidgets.QLabel(self.centralwidget)
        self.Graph.setGeometry(QtCore.QRect(490, 140, 320, 240))
        self.Graph.setStyleSheet(CSS.DefaultPicturesCSS)
        self.Graph.setText("")
        self.Graph.setObjectName("Graph")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(440, 10, 20, 521))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.SaveModelButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveModelButton.setGeometry(QtCore.QRect(780, 480, 41, 31))
        self.SaveModelButton.setObjectName("SaveButton")
        self.SaveModelButton.setStyleSheet(CSS.SaveButtonCSS)

        self.OriginalImageText = QtWidgets.QLabel(self.centralwidget)
        self.OriginalImageText.setGeometry(QtCore.QRect(65, 40, 121, 31))
        self.OriginalImageText.setObjectName("SaveAsText")

        self.GeneratedImage = QtWidgets.QLabel(self.centralwidget)
        self.GeneratedImage.setGeometry(QtCore.QRect(270, 40, 131, 31))
        self.GeneratedImage.setObjectName("HappyIcon")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Train Model"))
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
        self.EpochLoss.setText(_translate("MainWindow", "Epoch Loss:"))
        self.TotalTrainingLoss.setText(_translate("MainWindow", "Training Loss:"))
        self.ModelNameText.setText(_translate("MainWindow", "Model Name:"))
        self.OriginalImageText.setText(_translate("MainWindow", "Original Image"))
        self.GeneratedImage.setText(_translate("MainWindow", "Generated Image"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(CSS.BackgroundCSS)
        self.setWindowIcon(QIcon('Icons/TrainingIcon.png'))
        self.enableVariables(True)
        self.ModelName.setEnabled(False)
        self.SaveModelButton.setEnabled(False)
        self.ModelNameText.setEnabled(False)
        self.StopButton.setEnabled(False)
        self.ImportDataButton.clicked.connect(self.ImportData)
        self.ImportImagesButton.clicked.connect(self.ImportImages)
        self.StartButton.clicked.connect(self.StartTraining)
        self.StopButton.clicked.connect(self.StopTraining)
        self.StopButton.clicked.connect(self.OpenTrainingStoppedPage)
        self.SaveModelButton.clicked.connect(self.SaveModel)
        self.progressBar.valueChanged.connect(self.updateVariablesStatus)

    def ImportData(self):
        filename = QFileDialog.getOpenFileName(self, 'Import data',
                                               'Data Sets', " Excel File *.xlsx")
        path = filename[0]
        self.ImportDataPath.setText(path)

    def ImportImages(self):
        filename = str(QFileDialog.getExistingDirectory(self, "Import images", 'Raw Data'))
        path = filename
        print(path)
        self.ImportImagesPath.setText(path)

    def updateVariablesStatus(self):
        if 0 < self.progressBar.value() < 100:
            self.StopButton.setEnabled(True)
        if self.progressBar.value() == 0:
            self.enableVariables(True)
        else:
            self.enableVariables(False)

        if self.progressBar.value() == 100:
            self.ModelName.setEnabled(True)
            self.ModelNameText.setEnabled(True)
            self.SaveModelButton.setEnabled(True)
            self.ModelNameText.setEnabled(True)
            self.progressBar.setValue(0)

    def StartTraining(self):
        self.Graph.setStyleSheet(CSS.ClearImage)
        self.OriginalImage.setStyleSheet(CSS.ClearImage)
        self.NewImage.setStyleSheet(CSS.ClearImage)
        self.EpochLoss.setText("Epoch Loss: ")
        self.TotalTrainingLoss.setText("Training Loss: ")
        self.SaveModelButton.setEnabled(False)
        self.ModelNameText.setEnabled(False)
        self.ModelName.setText("")
        self.ModelName.setEnabled(False)
        if self.ImportDataPath.text() == "" or self.ImportImagesPath.text() == "":
            self.DataErrorPopUp()
            self.enableVariables(True)
        else:
            self.ValidateFiles()
            self.enableVariables(False)
            file = open("Temp files/CorrectImportFilesRecieved.txt", "r")
            CorrectDataSet = file.readline().strip()
            CorrectImageFolder = file.readline().strip()
            print("CorrectDataSet" + CorrectDataSet)
            print("CorrectImageFolder" + CorrectImageFolder)
            file.close()

            if CorrectDataSet == "0" or CorrectImageFolder == "0":
                self.error()
                self.enableVariables(True)

    def StopTraining(self):
        self.progressBar.setValue(100)
        self.updateVariablesStatus()
        file = open("Temp files/StopTrainingFlag.txt", "w")
        file.write("1")
        file.close()

    def ValidateFiles(self):
        file = open("Temp files/CorrectImportFilesRecieved.txt", "w")
        try:
            extract.main(
                self.ImportDataPath.text())
            CorrectDataPath = 1
        except:
            print("Could not load data from given Excel file.")
            CorrectDataPath = 0

        if len(os.listdir(self.ImportImagesPath.text())) == 0:
            CorrectImagePath = 0
        else:
            for fname in os.listdir(self.ImportImagesPath.text()):
                if fname.endswith('.BMT'):
                    CorrectImagePath = 1
                    break
                else:
                    print('Folder does not contain any BMT files')
                    CorrectImagePath = 0
                    break
        print(CorrectDataPath)
        print(CorrectImagePath)
        file.write(str(CorrectDataPath) + "\n")
        file.write(str(CorrectImagePath) + "\n")
        file.close()
        if CorrectImagePath == 1 and CorrectDataPath == 1:
            self.worker = MainBackgroundThread(self.ImportDataPath.text(), self.ImportImagesPath.text(),
                                               self.Epoch.text(),
                                               self.TrainingMode.currentText(), self.TrainingRatio.text(),
                                               self.LearningRate.text(),
                                               self.Momentum.text(), self.NewImage, self.OriginalImage,
                                               self.progressBar,
                                               self.Graph, self.EpochLoss, self.TotalTrainingLoss)
            self.worker.start()

    def DataErrorPopUp(self):
        self.window = QtWidgets.QMainWindow()
        self.window = TrainingPageDataErrorPopUp.MyWindow()
        self.window.show()

    def error(self):
        self.window = QtWidgets.QMainWindow()
        self.window = WrongFileImportedError.MyWindow()
        self.window.show()

    def ModelNameError(self):
        self.window = QtWidgets.QMainWindow()
        self.window = ErrorModelName.MyWindow()
        self.window.show()

    def OpenSaveModelPopUp(self):
        self.window = QtWidgets.QMainWindow()
        self.window = SaveModelPopUp.MyWindow()
        self.window.show()

    def OpenTrainingStoppedPage(self):
        self.window = QtWidgets.QMainWindow()
        self.window = TrainingStoppedPage.MyWindow()
        self.window.show()

    def OpenReplaceFileWindow(self):
        file = open("Temp files/ModelName.txt", "w")
        print(self.ModelName.text())
        file.write(self.ModelName.text())
        file.close()
        self.window = QtWidgets.QMainWindow()
        self.window = ReplaceFileWindow.MyWindow()
        self.window.show()
        self.window.YesButton.clicked.connect(self.SaveFile)

    def SaveFile(self):
        save_model(self.ModelName.text())
        file = open("Temp files/ModelName.txt", "w")
        print(self.ModelName.text())
        file.write(self.ModelName.text())
        file.close()
        self.OpenSaveModelPopUp()

    def SaveModel(self):
        found = 0
        if self.ModelName.text().isalnum():
            for fname in os.listdir("Models"):
                if fname == self.ModelName.text():
                    found = 1
            if found == 1:
                self.OpenReplaceFileWindow()
            else:
                self.SaveFile()
        else:
            self.ModelNameError()

    def enableVariables(self, boolean):
        self.Epoch.setEnabled(boolean)
        self.TrainingMode.setEnabled(boolean)
        self.TrainingRatio.setEnabled(boolean)
        self.LearningRate.setEnabled(boolean)
        self.Momentum.setEnabled(boolean)
        self.ImportImagesButton.setEnabled(boolean)
        self.ImportDataButton.setEnabled(boolean)

    def closeEvent(self, event):
        self.StopTraining()
        self.window = QtWidgets.QMainWindow()
        self.window = TrainingPageDataErrorPopUp.MyWindow()
        self.window.close()

        self.window = QtWidgets.QMainWindow()
        self.window = WrongFileImportedError.MyWindow()
        self.window.close()

        self.window = QtWidgets.QMainWindow()
        self.window = ErrorModelName.MyWindow()
        self.window.close()

        self.window = QtWidgets.QMainWindow()
        self.window = SaveModelPopUp.MyWindow()
        self.window.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
