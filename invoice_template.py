from fpdf import FPDF

class invoice(FPDF):

    def __init__(self):
        super().__init__(orientation = 'landscape', format = 'letter')

    def header(self):
        self.set_font('helvetica', 'BI', 12)
        self.cell(30, None, 'Institute for Quantitative Health Science and Engineering (IQ)', align = 'L')
        self.set_font('helvetica', 'B', 15)
        self.set_text_color(175, 175, 175)
        self.cell(0, None, "INVOICE", align = 'R')
        self.ln(6)
        self.set_font('helvetica', 'BI', 10)
        self.set_text_color(0, 0, 0)
        self.cell(30, None, '3D Printing Core', align = 'L')
        self.ln(6)
        self.set_font('helvetica', '', 8)
        self.multi_cell(0, None, 'Michigan State University\n775 Woodlot Drive, IQ Building\nEast Lansing, MI 48824', align = 'L')


    def footer(self):
        self.set_y(-30)
        self.set_font("helvetica", 'BI', 10)
        self.cell(0, None, 'Contact Information:', align = 'C')
        self.ln(5)
        self.set_font('helvetica', '', 10)
        self.multi_cell(0, None, 'Stephen Branch\nPhone: (517) 353-1116\nEmail: branchs1@msu.edu', align = 'C')
        self.ln(6)
        self.set_font('helvetica', 'B', 12)
        self.cell(0, None, 'Thank you for using IQ Core services!', align = 'C')