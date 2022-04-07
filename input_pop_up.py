from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
import ErrorPopUp
import integration
import CSS


class Ui_MainWindow(QObject):

    # Set up test model UI page.
    def setupUi(self, Form):
        Form.setWindowIcon(QIcon('TestIcon.png'))
        Form.setObjectName("Form")
        Form.setFixedSize(690, 389)
        Form.setStyleSheet(CSS.BackgroundCSS)

        self.SubmitButton = QtWidgets.QPushButton(Form)
        self.SubmitButton.setGeometry(QtCore.QRect(520, 350, 141, 31))
        self.SubmitButton.clicked.connect(self.SubmitAction)
        self.SubmitButton.setStyleSheet(CSS.QPushButtonCSS)
        self.SubmitButton.setObjectName("SubmitButton")

        font = self.fontSetting()

        self.ParafinWaxText = QtWidgets.QLabel(Form)
        self.ParafinWaxText.setGeometry(QtCore.QRect(470, 139, 121, 21))
        self.ParafinWaxText.setFont(font)
        self.ParafinWaxText.setObjectName("ParafinWaxText")

        self.TemperatureText = QtWidgets.QLabel(Form)
        self.TemperatureText.setGeometry(QtCore.QRect(100, 19, 121, 41))
        self.TemperatureText.setFont(font)
        self.TemperatureText.setObjectName("TemperatureText")

        self.StearicAcidWaxCompositionText = QtWidgets.QLabel(Form)
        self.StearicAcidWaxCompositionText.setGeometry(QtCore.QRect(330, 259, 261, 21))
        self.StearicAcidWaxCompositionText.setFont(font)
        self.StearicAcidWaxCompositionText.setObjectName("StearicAcidWaxCompositionText")

        self.LauricAcidText = QtWidgets.QLabel(Form)
        self.LauricAcidText.setGeometry(QtCore.QRect(490, 19, 101, 21))
        self.LauricAcidText.setFont(font)
        self.LauricAcidText.setObjectName("LauricAcidText")

        self.WindSpeed = QtWidgets.QSpinBox(Form)
        self.WindSpeed.setGeometry(QtCore.QRect(230, 140, 71, 31))
        self.WindSpeed.setStyleSheet(CSS.QSpinBoxCSS)
        self.WindSpeed.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.WindSpeed.setAccelerated(True)
        self.WindSpeed.setMaximum(99)
        self.WindSpeed.setObjectName("WindSpeed")

        self.LauricAcidComp = QtWidgets.QSpinBox(Form)
        self.LauricAcidComp.setGeometry(QtCore.QRect(600, 189, 71, 31))
        self.LauricAcidComp.setStyleSheet(CSS.QSpinBoxCSS)
        self.LauricAcidComp.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.LauricAcidComp.setAccelerated(True)
        self.LauricAcidComp.setMaximum(3)
        self.LauricAcidComp.setObjectName("LauricAcidComp")

        self.LauricAcid = QtWidgets.QSpinBox(Form)
        self.LauricAcid.setGeometry(QtCore.QRect(600, 9, 71, 31))
        self.LauricAcid.setStyleSheet(CSS.QSpinBoxCSS)
        self.LauricAcid.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.LauricAcid.setAccelerated(True)
        self.LauricAcid.setMaximum(1)
        self.LauricAcid.setObjectName("LauricAcid")

        self.ChemicalTemperatureText = QtWidgets.QLabel(Form)
        self.ChemicalTemperatureText.setGeometry(QtCore.QRect(20, 270, 201, 21))
        self.ChemicalTemperatureText.setFont(font)
        self.ChemicalTemperatureText.setObjectName("ChemicalTemperatureText")

        self.ParafinWaxComp = QtWidgets.QSpinBox(Form)
        self.ParafinWaxComp.setGeometry(QtCore.QRect(600, 310, 71, 31))
        self.ParafinWaxComp.setStyleSheet(CSS.QSpinBoxCSS)
        self.ParafinWaxComp.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ParafinWaxComp.setAccelerated(True)
        self.ParafinWaxComp.setMaximum(3)
        self.ParafinWaxComp.setObjectName("ParafinWaxComp")

        self.StearicAcidText = QtWidgets.QLabel(Form)
        self.StearicAcidText.setGeometry(QtCore.QRect(480, 79, 111, 21))
        self.StearicAcidText.setFont(font)
        self.StearicAcidText.setObjectName("StearicAcidText")

        self.Humidity = QtWidgets.QDoubleSpinBox(Form)
        self.Humidity.setGeometry(QtCore.QRect(230, 80, 71, 31))
        self.Humidity.setStyleSheet(CSS.QDoubleSpinBoxCSS)
        self.Humidity.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.Humidity.setAccelerated(True)
        self.Humidity.setDecimals(1)
        self.Humidity.setObjectName("Humidity")

        self.WindSpeedText = QtWidgets.QLabel(Form)
        self.WindSpeedText.setGeometry(QtCore.QRect(110, 150, 101, 21))
        self.WindSpeedText.setFont(font)
        self.WindSpeedText.setObjectName("WindSpeedText")

        self.ParafinWaxCompositionText = QtWidgets.QLabel(Form)
        self.ParafinWaxCompositionText.setGeometry(QtCore.QRect(370, 319, 221, 21))
        self.ParafinWaxCompositionText.setFont(font)
        self.ParafinWaxCompositionText.setObjectName("ParafinWaxCompositionText")

        self.StearicAcidWaxComp = QtWidgets.QSpinBox(Form)
        self.StearicAcidWaxComp.setGeometry(QtCore.QRect(600, 249, 71, 31))
        self.StearicAcidWaxComp.setStyleSheet(CSS.QSpinBoxCSS)
        self.StearicAcidWaxComp.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.StearicAcidWaxComp.setAccelerated(True)
        self.StearicAcidWaxComp.setMaximum(3)
        self.StearicAcidWaxComp.setObjectName("StearicAcidWaxComp")

        self.ChemicalTemp = QtWidgets.QDoubleSpinBox(Form)
        self.ChemicalTemp.setGeometry(QtCore.QRect(230, 260, 71, 31))
        self.ChemicalTemp.setStyleSheet(CSS.QDoubleSpinBoxCSS)
        self.ChemicalTemp.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ChemicalTemp.setAccelerated(True)
        self.ChemicalTemp.setDecimals(1)
        self.ChemicalTemp.setMinimum(15.0)
        self.ChemicalTemp.setMaximum(55.0)
        self.ChemicalTemp.setObjectName("ChemicalTemp")

        self.Temperature = QtWidgets.QDoubleSpinBox(Form)
        self.Temperature.setGeometry(QtCore.QRect(230, 20, 71, 31))
        self.Temperature.setStyleSheet(CSS.QDoubleSpinBoxCSS)
        self.Temperature.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.Temperature.setAccelerated(True)
        self.Temperature.setDecimals(1)
        self.Temperature.setMinimum(15.0)
        self.Temperature.setMaximum(45.0)
        self.Temperature.setProperty("value", 15.0)
        self.Temperature.setObjectName("Temperature")

        self.HumidityText = QtWidgets.QLabel(Form)
        self.HumidityText.setGeometry(QtCore.QRect(130, 79, 91, 41))
        self.HumidityText.setFont(font)
        self.HumidityText.setObjectName("label_3")

        self.AluminiumTemperatureText = QtWidgets.QLabel(Form)
        self.AluminiumTemperatureText.setGeometry(QtCore.QRect(10, 210, 211, 21))
        self.AluminiumTemperatureText.setFont(font)
        self.AluminiumTemperatureText.setObjectName("label_6")

        self.ParafinWax = QtWidgets.QSpinBox(Form)
        self.ParafinWax.setGeometry(QtCore.QRect(600, 129, 71, 31))
        self.ParafinWax.setStyleSheet(CSS.QSpinBoxCSS)
        self.ParafinWax.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ParafinWax.setAccelerated(True)
        self.ParafinWax.setMaximum(1)
        self.ParafinWax.setObjectName("ParafinWax")

        self.LauricAcidComposition = QtWidgets.QLabel(Form)
        self.LauricAcidComposition.setGeometry(QtCore.QRect(380, 199, 211, 21))
        self.LauricAcidComposition.setFont(font)
        self.LauricAcidComposition.setObjectName("LauricAcidComposition")

        self.AluminiumTemp = QtWidgets.QDoubleSpinBox(Form)
        self.AluminiumTemp.setGeometry(QtCore.QRect(230, 200, 71, 31))
        self.AluminiumTemp.setStyleSheet(CSS.QDoubleSpinBoxCSS)
        self.AluminiumTemp.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.AluminiumTemp.setAccelerated(True)
        self.AluminiumTemp.setDecimals(1)
        self.AluminiumTemp.setMinimum(15.0)
        self.AluminiumTemp.setMaximum(55.0)
        self.AluminiumTemp.setProperty("value", 15.0)
        self.AluminiumTemp.setObjectName("AluminiumTemp")

        self.StearicAcid = QtWidgets.QSpinBox(Form)
        self.StearicAcid.setGeometry(QtCore.QRect(600, 69, 71, 31))
        self.StearicAcid.setStyleSheet(CSS.QSpinBoxCSS)
        self.StearicAcid.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.StearicAcid.setAccelerated(True)
        self.StearicAcid.setMaximum(1)
        self.StearicAcid.setObjectName("StearicAcid")

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(310, 20, 20, 351))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # font setting
    def fontSetting(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        return font

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test Model"))
        self.SubmitButton.setText(_translate("Form", "Submit"))
        self.ParafinWaxText.setText(_translate("Form", "Parafin Wax :"))
        self.TemperatureText.setText(_translate("Form", "Temperature :"))
        self.StearicAcidWaxCompositionText.setText(_translate("Form", "Stearic Acid Wax Composition :"))
        self.LauricAcidText.setText(_translate("Form", "Lauric Acid :"))
        self.ChemicalTemperatureText.setText(_translate("Form", "Chemical Temperature :"))
        self.StearicAcidText.setText(_translate("Form", "Stearic Acid :"))
        self.WindSpeedText.setText(_translate("Form", "Windspeed :"))
        self.ParafinWaxCompositionText.setText(_translate("Form", "Parafin Wax Composition :"))
        self.HumidityText.setText(_translate("Form", "Humidity :"))
        self.AluminiumTemperatureText.setText(_translate("Form", "Aluminium Temperature :"))
        self.LauricAcidComposition.setText(_translate("Form", "Lauric Acid Composition :"))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # ++++
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.enableLauricAcid(False)
        self.enableStearicAcid(False)
        self.enableParafinWax(False)
        self.LauricAcid.valueChanged.connect(self.updateLauricAcid)
        self.StearicAcid.valueChanged.connect(self.updateStearicAcid)
        self.ParafinWax.valueChanged.connect(self.updateParafinWax)

    # If lauric acid is 1, then it gives the user the option to alter lauric acid composition.
    def updateLauricAcid(self):
        if self.LauricAcid.text() == '1':
            self.enableLauricAcid(True)
        else:
            self.LauricAcidComp.setValue(0)
            self.enableLauricAcid(False)

    # If stearic acid is 1, then it gives the user the option to alter stearic acid composition.
    def updateStearicAcid(self):
        if self.StearicAcid.text() == '1':
            self.enableStearicAcid(True)
        else:
            self.StearicAcidWaxComp.setValue(0)
            self.enableStearicAcid(False)

    # If parafin wax is 1, then it gives the user the option to alter parafin wax composition.
    def updateParafinWax(self):
        if self.ParafinWax.text() == '1':
            self.enableParafinWax(True)
        else:
            self.ParafinWaxComp.setValue(0)
            self.enableParafinWax(False)

    # ability to lock or give access to lauric acid composition.
    def enableLauricAcid(self, boolean):
        self.LauricAcidComp.setEnabled(boolean)
        self.LauricAcidComposition.setEnabled(boolean)

    # ability to lock or give access to stearic acid composition.
    def enableStearicAcid(self, boolean):
        self.StearicAcidWaxComp.setEnabled(boolean)
        self.StearicAcidWaxCompositionText.setEnabled(boolean)

    # ability to lock or give access to parafin wax composition.
    def enableParafinWax(self, boolean):
        self.ParafinWaxComp.setEnabled(boolean)
        self.ParafinWaxCompositionText.setEnabled(boolean)

    # When user clicks submit, the program checks if the correct trained model is loaded and if the correct model is
    # loaded it shows a heatmap on the main screen.
    def SubmitAction(self):
        integration.main('Data.xlsx')
        integration.set_data(self.Temperature.text(), self.Humidity.text(), self.WindSpeed.text(),
                             self.AluminiumTemp.text(), self.ChemicalTemp.text(), self.LauricAcid.text(),
                             self.StearicAcid.text(),
                             self.ParafinWax.text(), self.LauricAcidComp.text(), self.StearicAcidWaxComp.text(),
                             self.ParafinWaxComp.text())
        file = open("CorrectFileReceived.txt", 'r')
        CorrectFileReceived = file.read()
        file.close()
        if CorrectFileReceived == '0':
            self.window = QtWidgets.QMainWindow()
            self.window = ErrorPopUp.MyWindow()
            self.window.show()

        with open("Variables.txt", 'w') as file:
            file.write(self.Temperature.text() + " °C" + "\n")
            file.write(self.Humidity.text() + " %" + "\n")
            file.write(self.WindSpeed.text() + " km/hr" + "\n")
            file.write(self.AluminiumTemp.text() + " °C" + "\n")
            file.write(self.ChemicalTemp.text() + " °C" + "\n")
            file.write(self.LauricAcid.text() + "\n")
            file.write(self.StearicAcid.text() + "\n")
            file.write(self.ParafinWax.text() + "\n")
            file.write(self.LauricAcidComp.text() + "\n")
            file.write(self.StearicAcidWaxComp.text() + "\n")
            file.write(self.ParafinWaxComp.text() + "\n")
        file.close()
