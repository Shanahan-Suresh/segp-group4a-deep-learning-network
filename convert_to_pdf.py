import os

from PyQt5.QtWidgets import QFileDialog
from fpdf import FPDF


# Code to generate the required PDF file
def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=15)
    pdf.image(name="Icons/nottinghamlogo.jpeg", x=5, y=5, w=70, h=25)
    pdf.cell(0, 60, txt="Generated Heat Map",
             ln=1, align='C')
    pdf.image(name="Temp files/temp.png", x=50, y=60, w=110, h=80)
    epw = pdf.w - 2 * pdf.l_margin
    col_width = epw / 2

    file = open('Temp files/Variables.txt', 'r')

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

    pdf.set_font('Times', '', 10.0)
    pdf.ln(0.5)
    th = pdf.font_size
    pdf.ln(27.5 * th)
    pdf.set_font('Times', '', 10.0)
    for row in data:
        for datum in row:
            pdf.cell(col_width, 2 * th, str(datum), border=1)
        pdf.ln(2 * th)
    PDFfile, check = QFileDialog.getSaveFileName(None, "Save As Report",
                                                 "Reports", "PDF (*.pdf)")
    if check:
        print(PDFfile)
        pdf.output(PDFfile, 'F')
        os.startfile(PDFfile)
