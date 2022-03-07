# Python program to create
# a pdf file


from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)

# create a cell
pdf.cell(200, 10, txt="Heat Map",  # main title
		 ln=1, align='C')

pdf.image(name="temp.png", x=10, y=20, w=80, h=80)

#***************************************

# Effective page width, or just epw
epw = pdf.w - 2 * pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content
# evenly across table and page
col_width = epw / 2

# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.
file = open('Variables.txt', 'r')
data = [['Temperature', file.readline().strip()],
		['Humidity', file.readline().strip()],
		['WindSpeed', file.readline().strip()],
		['SR File Number', file.readline().strip()],
		['Aluminum Temperature', file.readline().strip()],
		['Chemical Temperature', file.readline().strip()],
		['Lauric Acid', file.readline().strip()],
		['Stearic Acid', file.readline().strip()],
		['Parafin Wax', file.readline().strip()],
		['Lauric Acid Composition', file.readline().strip()],
		['Stearic Acid Wax Composition', file.readline().strip()],
		['Parafin Wax Composition', file.readline().strip()]
		]
file.close()

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

#***************************************
# save the pdf with name .pdf
pdf.output('GFG.pdf', 'F')
