import os

import CSS
import load_model
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QHeaderView, QFileDialog, QApplication
from PyQt5.QtGui import QIcon
from fpdf import FPDF
import input_pop_up
import training_page
from additional_features import main as additional_features_main

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def format_cursor_data(data):
    if data[0] > 0.45 and data[1] >= 0.45:
        return "[" + str(round((13 * data[0] + 8 * data[1] + 5.6 * data[2]), 2)) + "]"
    if data[0] < 0.1 and data[1] >= data[2]:
        if (data[1] - data[2] >= 0.2):
            return "[" + str(round((15 * data[0] + 14 * data[1] + 5 * data[2]), 2)) + "]"
        else:
            return "[" + str(round((15 * data[0] + 12 * data[1] + 4 * data[2]), 2)) + "]"
    return "[" + str(round((23 * data[0] + 10 * data[1] + 6 * data[2]), 2)) + "]"


def ConvertToPdf():
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # create a cell
    pdf.cell(200, 10, txt="Heat Map",  # main title
             ln=1, align='C')

    pdf.image(name="temp.png", x=50, y=20, w=110, h=80)

    # ***************************************

    # Effective page width, or just epw
    epw = pdf.w - 2 * pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw / 2

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.
    file = open('Variables.txt', 'r')
    Temperature = file.readline().strip()
    Humidity = file.readline().strip()
    WindSpeed = file.readline().strip()
    AluminumTemperature = file.readline().strip()
    ChemicalTemperature = file.readline().strip()
    LauricAcid = file.readline().strip()
    StearicAcid = file.readline().strip()
    ParafinWax = file.readline().strip()
    LauricAcidComposition = file.readline().strip()
    StearicAcidWaxComposition = file.readline().strip()
    ParafinWaxComposition = file.readline().strip()
    file.close()
    data = [['Temperature', Temperature],
            ['Humidity', Humidity],
            ['WindSpeed', WindSpeed],
            ['Aluminum Temperature', AluminumTemperature],
            ['Chemical Temperature', ChemicalTemperature],
            ['Lauric Acid', LauricAcid],
            ['Stearic Acid', StearicAcid],
            ['Parafin Wax', ParafinWax],
            ['Lauric Acid Composition', LauricAcidComposition],
            ['Stearic Acid Wax Composition', StearicAcidWaxComposition],
            ['Parafin Wax Composition', ParafinWaxComposition]
            ]
    # Document title centered, 'B'old, 14 pt
    pdf.set_font('Times', 'B', 14.0)
    pdf.set_font('Times', '', 10.0)
    pdf.ln(0.5)

    # Text height is the same as current font size
    th = pdf.font_size

    # Line break equivalent to 4 lines
    pdf.ln(20 * th)

    # Line break equivalent to 4 lines
    pdf.ln(4 * th)

    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, 'Report', align='C')
    pdf.ln(th)
    pdf.set_font('Times', '', 10.0)
    pdf.ln(0.5)

    # Here we add more padding by passing 2*th as height
    for row in data:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width, 2 * th, str(datum), border=1)

        pdf.ln(2 * th)

    # ***************************************
    # save the pdf with name .pdf
    PDFfile, check = QFileDialog.getSaveFileName(None, "Save As Report",
                                                 "", "PDF (*.pdf)")
    if check:
        print(PDFfile)
        pdf.output(PDFfile, 'F')
        os.startfile(PDFfile)

class Ui_MainWindow(QObject):

    def setupUi(self, MainWindow):
        self.ClearFile()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1154, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InitializeTable()
        self.Table()

        self.heatMapButton = QtWidgets.QPushButton(self.centralwidget)
        self.heatMapButton.setGeometry(QtCore.QRect(460, 120, 666, 500))
        self.heatMapButton.setStyleSheet(CSS.DefaultHeatmapCSS)
        self.heatMapButton.setObjectName("pushButton")

        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(10, 620, 51, 41))
        self.editButton.setStyleSheet(CSS.EditIconCSS)
        self.editButton.setText("")
        self.editButton.setObjectName("pushButton_2")

        self.NottinghamLogo = QtWidgets.QLabel(self.centralwidget)
        self.NottinghamLogo.setGeometry(QtCore.QRect(-20, 0, 1171, 101))
        self.NottinghamLogo.setStyleSheet(CSS.MainPageLogo)
        self.NottinghamLogo.setObjectName("NottinghamLogo")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 1154, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)

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
        self.actionSave_as.setIcon(QtGui.QIcon('ReportIcon.png'))
        self.actionSave_as.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionSave_as.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.setEnabled(False)
        self.actionSave_as.triggered.connect(ConvertToPdf)

        self.actionTest_model = QtWidgets.QAction(MainWindow)
        self.actionTest_model.setIcon(QtGui.QIcon('TestIcon.png'))
        self.actionTest_model.setCheckable(False)
        self.actionTest_model.setChecked(False)
        self.actionTest_model.setObjectName("actionTest_model")

        self.actionExtract_Image = QtWidgets.QAction(MainWindow)
        self.actionExtract_Image.setIcon(QtGui.QIcon('ExtractIcon.png'))
        self.actionExtract_Image.setObjectName("actionExtract_Image")
        self.actionExtract_Image.triggered.connect(self.ExtractImage)
        self.actionExtract_Image.setEnabled(False)

        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setIcon(QtGui.QIcon('ExtractIcon.png'))
        self.actionSave_Image.setObjectName("actionSave_Image")

        self.actionTrain_Model = QtWidgets.QAction(MainWindow)
        self.actionTrain_Model.setObjectName("actionTrain_Model")
        self.actionTrain_Model.setIcon(QtGui.QIcon('TrainingIcon.png'))

        self.selectModel = QtWidgets.QAction(MainWindow)
        self.selectModel.setObjectName("actionSimulate_Model")
        self.selectModel.setIcon(QtGui.QIcon('SelectModelIcon.png'))

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.actionTrain_Model.setStatusTip(_translate("MainWindow", "Train Model"))
        self.selectModel.setText(_translate("MainWindow", "Select Model"))
        self.selectModel.setStatusTip(_translate("MainWindow", "Select Model"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('MainNotLogo.jpg'))
        self.setStyleSheet(CSS.BackgroundCSS)
        self.menuBar.setStyleSheet(CSS.MenuBarCSS)
        self.actionTest_model.triggered.connect(self.openTestWindow)
        self.actionTrain_Model.triggered.connect(self.openTrainWindow)
        self.selectModel.triggered.connect(self.openLoadWindow)
        self.editButton.clicked.connect(self.openTestWindow)

    def updateMainWindow(self):
        file = open("CorrectFileReceived.txt", 'r')
        CorrectFileReceived = file.read()
        file.close()
        if CorrectFileReceived == '1':
            self.enableOptions(True)
        else:
            self.enableOptions(False)
        self.Table()
        self.window.close()

    def openTestWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window = input_pop_up.MyWindow()
        self.window.show()
        self.window.SubmitButton.clicked.connect(self.updateMainWindow)

    def openTrainWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window = training_page.MyWindow()
        self.window.show()

    def openLoadWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window = load_model.MyWindow()
        self.window.show()

    def enableOptions(self, boolean):
        self.actionSave_as.setEnabled(boolean)
        self.actionExtract_Image.setEnabled(boolean)
        self.heatMapButton.setEnabled(boolean)
        if boolean == True:
            self.heatMapButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.heatMapButton.setStyleSheet(CSS.HeatMapCSS)
            self.heatMapButton.clicked.connect(self.ExtractImage)
        else:
            self.heatMapButton.setStyleSheet(CSS.DefaultHeatmapCSS)
            file = open('Variables.txt', 'w')
            file.close()

    def Table(self):
        file = open('Variables.txt', 'r')
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Temperature")
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 1
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Humidity")
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(file.readline().strip())  # 2
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Wind Speed")
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 3
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Aluminium Temperature")
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 5
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Chemical Temperature")
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 6
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Lauric Acid")
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 7
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Stearic Acid")
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 8
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Parafin Wax")
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 9
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Lauric Acid Composition")
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 10
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Stearic Acid Wax Composition")
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 11
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText("Parafin Wax Composition")
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        item.setText(file.readline().strip())  # 12
        self.tableWidget.setItem(10, 1, item)
        file.close()

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

    def ClearFile(self):
        file = open("variables.txt", 'w')
        file.close()
        file1 = open("Path.txt", 'w')
        file1.write('PreInstalledModel')
        file1.close()

    def ExtractImage(self):
        additional_features_main()

    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
