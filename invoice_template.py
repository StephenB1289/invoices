from fpdf import FPDF
from requests import head

class invoice(FPDF):

    def __init__(self):
        super().__init__(orientation = 'landscape', format = 'letter')

    def header(self):
        self.set_font('helvetica', 'B', 14)
        header_text = 'Institute for Quantitative Health Science and Engineering (IQ)'
        self.cell(self.get_string_width(header_text), None, header_text, align = 'L')
        self.set_font('helvetica', 'B', 35)
        self.set_text_color(175, 175, 175)
        self.cell(0, 25, "INVOICE", align = 'C')
        self.ln(6)
        self.set_font('helvetica', 'BI', 12)
        self.set_text_color(0, 0, 0)
        self.cell(30, None, '3D Printing Core', align = 'L')
        self.ln(6)
        self.set_font('helvetica', '', 8)
        self.multi_cell(0, 4, 'Michigan State University\n775 Woodlot Drive, IQ Building\nEast Lansing, MI 48824', align = 'L')
        self.ln(10)


    def footer(self):
        self.set_y(-30)
        self.set_font("helvetica", 'B', 10)
        self.cell(0, None, 'Contact Information:', align = 'C')
        self.ln(5)
        self.set_font('helvetica', '', 10)
        self.multi_cell(0, None, 'Stephen Branch\nPhone: (517) 353-1116\nEmail: branchs1@msu.edu', align = 'C')
        self.ln(6)
        self.set_font('helvetica', 'B', 12)
        self.cell(0, None, 'Thank you for using IQ Core services!', align = 'C')