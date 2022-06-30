from fpdf import FPDF

class invoice(FPDF):

    def __init__(self):
        super().__init__(orientation = 'landscape', format = 'letter')

    def header(self):
        self.set_font('helvetica', 'BI', 12)
        self.cell(30, 10, 'Institute for Quantitative Health Science and Engineering (IQ)', align = 'L')
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(175, 175, 175)
        self.cell(0, 10, "INVOICE", align = 'R')
        self.ln(5)
        self.set_font('helvetica', 'BI', 10)
        self.set_text_color(0, 0, 0)
        self.cell(30, 10, '3D Printing Core', align = 'L')


    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
