import os
import CSS
import load_model
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QHeaderView, QApplication
from PyQt5.QtGui import QIcon
import input_pop_up
import training_page
from additional_features import main as additional_features_main
from ConvertToPDF import main as ConvertToPdf

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


# Clear the variable file and add the preinstalled model to path.txt
def ClearFile():
    ClearVariableFile()
    LoadPreInstalledModel()


# File containing name of pre installed model
def LoadPreInstalledModel():
    file = open("Temp files/Path.txt", 'w')
    file.write('PreInstalledModel')
    file.close()


# Extract image and use line to see temperature in the line
def ExtractImage():
    additional_features_main()


# Deletes everything from variables file
def ClearVariableFile():
    file = open('Temp files/Variables.txt', 'w')
    file.close()


class Ui_MainWindow(QObject):
    # Set up the main page of the gui
    def setupUi(self, MainWindow):
        ClearFile()

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1154, 723)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.InitializeTable()
        self.ShowUpdatedTable()

        self.heatMap = QtWidgets.QPushButton(self.centralwidget)
        self.heatMap.setGeometry(QtCore.QRect(460, 120, 666, 500))
        self.heatMap.setStyleSheet(CSS.DefaultHeatmapCSS)
        self.heatMap.setObjectName("CloseButton")

        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(10, 620, 51, 41))
        self.editButton.setStyleSheet(CSS.EditIconCSS)
        self.editButton.setText("")
        self.editButton.setObjectName("LoadModelButton")
        self.editButton.setStatusTip("Test Model")

        self.NottinghamLogo = QtWidgets.QLabel(self.centralwidget)
        self.NottinghamLogo.setGeometry(QtCore.QRect(-20, 0, 1171, 101))
        self.NottinghamLogo.setStyleSheet(CSS.MainPageLogo)
        self.NottinghamLogo.setObjectName("NottinghamLogo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menuBar.setObjectName("menuBar")

        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        self.menuTest = QtWidgets.QMenu(self.menuBar)
        self.menuTest.setObjectName("menuTest")

        self.menuImage = QtWidgets.QMenu(self.menuBar)
        self.menuImage.setObjectName("menuImage")

        MainWindow.setMenuBar(self.menuBar)

        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setIcon(QtGui.QIcon('Icons/ReportIcon.png'))
        self.actionSave_as.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionSave_as.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.triggered.connect(ConvertToPdf)

        self.actionTest_model = QtWidgets.QAction(MainWindow)
        self.actionTest_model.setIcon(QtGui.QIcon('Icons/TestIcon.png'))
        self.actionTest_model.setCheckable(False)
        self.actionTest_model.setChecked(False)
        self.actionTest_model.setObjectName("actionTest_model")

        self.actionExtract_Image = QtWidgets.QAction(MainWindow)
        self.actionExtract_Image.setIcon(QtGui.QIcon('Icons/ExtractIcon.png'))
        self.actionExtract_Image.setObjectName("actionExtract_Image")
        self.actionExtract_Image.triggered.connect(ExtractImage)

        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setIcon(QtGui.QIcon('Icons/ExtractIcon.png'))
        self.actionSave_Image.setObjectName("actionSave_Image")

        self.actionTrain_Model = QtWidgets.QAction(MainWindow)
        self.actionTrain_Model.setObjectName("actionTrain_Model")
        self.actionTrain_Model.setIcon(QtGui.QIcon('Icons/TrainingIcon.png'))

        self.selectModel = QtWidgets.QAction(MainWindow)
        self.selectModel.setObjectName("actionSimulate_Model")
        self.selectModel.setIcon(QtGui.QIcon('Icons/SelectModelIcon.png'))

        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()

        self.menuTest.addAction(self.actionTest_model)
        self.menuTest.addAction(self.actionTrain_Model)
        self.menuTest.addAction(self.selectModel)

        self.menuImage.addAction(self.actionExtract_Image)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTest.menuAction())
        self.menuBar.addAction(self.menuImage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HeatGen"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Details:"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTest.setTitle(_translate("MainWindow", "Model"))
        self.menuImage.setTitle(_translate("MainWindow", "Image"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as Report"))
        self.actionSave_as.setStatusTip(_translate("MainWindow", "Save as Report"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionTest_model.setText(_translate("MainWindow", "Test Model"))
        self.actionTest_model.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionTest_model.setStatusTip(_translate("MainWindow", "Test Model"))
        self.actionExtract_Image.setText(_translate("MainWindow", "Extract Image"))
        self.actionExtract_Image.setStatusTip(_translate("MainWindow", "Extract Image"))
        self.actionExtract_Image.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionSave_Image.setStatusTip(_translate("MainWindow", "Save Image"))
        self.actionTrain_Model.setText(_translate("MainWindow", "Train Model"))
        self.actionTrain_Model.setShortcut(_translate("MainWindow", "Alt+T"))
        self.actionTrain_Model.setStatusTip(_translate("MainWindow", "Train Model"))
        self.selectModel.setText(_translate("MainWindow", "Select Model"))
        self.selectModel.setShortcut(_translate("MainWindow", "Alt+S"))
        self.selectModel.setStatusTip(_translate("MainWindow", "Select Model"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('Icons/MainNotLogo.jpg'))
        self.setStyleSheet(CSS.BackgroundCSS)
        self.menuBar.setStyleSheet(CSS.MenuBarCSS)

        self.enableOptions(False)
        self.actionTest_model.triggered.connect(self.openTestWindow)
        self.actionTrain_Model.triggered.connect(self.openTrainWindow)
        self.selectModel.triggered.connect(self.openLoadWindow)
        self.editButton.clicked.connect(self.openTestWindow)

    # Update main window when the model is tested
    def updateMainWindow(self):
        file = open("Temp files/CorrectFileReceived.txt", 'r')

        CorrectFileReceived = file.read()

        file.close()

        if CorrectFileReceived == '1':
            self.enableOptions(True)
        else:
            self.enableOptions(False)

        self.ShowUpdatedTable()
        self.window.close()

    # Open the test model window
    def openTestWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window = input_pop_up.MyWindow()
        self.window.show()
        self.window.SubmitButton.clicked.connect(self.updateMainWindow)

    # Open the train model window
    def openTrainWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window = training_page.MyWindow()
        self.window.show()

    # Open the load model window
    def openLoadWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window = load_model.MyWindow()
        self.window.show()

    # Enable or disable options(extract image, save as report)
    def enableOptions(self, boolean):
        self.actionSave_as.setEnabled(boolean)
        self.actionExtract_Image.setEnabled(boolean)
        self.heatMap.setEnabled(boolean)

        if boolean:

            self.heatMap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.heatMap.setStyleSheet(CSS.HeatMapCSS)
            self.heatMap.clicked.connect(ExtractImage)
            self.heatMap.setStatusTip("Extract Image")

        else:

            self.heatMap.setStatusTip("")
            self.heatMap.setStyleSheet(CSS.DefaultHeatmapCSS)
            ClearVariableFile()

    # Set up table for the main page
    def InitializeTable(self):
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 120, 411, 481))
        self.tableWidget.setStyleSheet(CSS.TableCSS)
        hheader = self.tableWidget.horizontalHeader()
        hheader.setSectionResizeMode(QHeaderView.Stretch)
        vheader = self.tableWidget.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

    # Put values inside the table of the main window
    def ShowUpdatedTable(self):
        file = open('Temp files/Variables.txt', 'r')

        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Temperature")
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Humidity")
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(file.readline().strip())
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Wind Speed")
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Aluminium Temperature")
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Chemical Temperature")
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Lauric Acid")
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Stearic Acid")
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Parafin Wax")
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Lauric Acid Composition")
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Stearic Acid Wax Composition")
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Parafin Wax Composition")
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())
        self.tableWidget.setItem(10, 1, item)

        file.close()

    # Close all windows when main window is closed
    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
