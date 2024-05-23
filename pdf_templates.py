from fpdf import FPDF
from datetime import date

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
        self.set_font('helvetica', 'B', 12)
        self.cell(0, None, 'Thank you for using IQ Core services!', align = 'C')

    def generate_invoice(self, details, charges, number):
        customer, lab, account = details

        self.add_page()
        self.set_font('helvetica', 'B', 10)
        self.cell(30, None, 'Bill to:', align = 'L')
        self.cell(190, None, 'Date:', align = 'R')
        self.set_font('helvetica', '', 10)
        self.cell(0, None, str(date.today()), align = 'R')
        self.ln(5)
        self.cell(30, None, f'{customer} ({lab} Lab)', align = 'L')
        self.set_font('helvetica', 'B', 10)
        self.cell(190, None, 'Invoice #:', align = 'R')
        self.set_font('helvetica', '', 10)
        self.cell(0, None, number, align = 'R')
        self.ln(5)
        self.cell(30, None, account, align = 'L')
        self.set_font('helvetica', 'B', 10)
        self.cell(190, None, 'Customer:', align = 'R')
        self.set_font('helvetica', '', 10)
        self.cell(0, None, customer, align = 'R')

        self.ln(15)

        self.set_font('helvetica', 'B', 10)
        self.cell(260/4, None, 'Description', align = 'C')
        self.cell(260/4, None, 'Rate', align = 'C')
        self.cell(260/4, None, 'Quantity', align = 'C')
        self.cell(260/4, None, 'Charge', align = 'C')

        self.ln(6)

        self.set_font('helvetica', '', 10)
        
        for i, item in enumerate(charges):
            if charges[i][2] != 0:
                self.cell(260/4, 5, charges[i][0], align = 'L', border = True)
                self.cell(260/4, 5, f'${charges[i][1]:.2f}', align = 'C', border = True)
                self.cell(260/4, 5, f'{charges[i][2]:.2f}', align = 'C', border = True)
                self.cell(260/4, 5, f'${charges[i][3]:.2f}', align = 'C', border = True)
                self.ln()

        self.ln()
        self.set_font('helvetica', 'B', 10)
        self.set_x(260/2 + 10)
        self.cell(260/4, None, 'Total:', align = 'C')
        self.cell(0, None, f'${sum([x[3] for x in charges]):.2f}', align = 'C')

        self.ln(6)

        self.set_line_width(1)
        self.set_draw_color(175, 175, 175)
        self.line(10, self.get_y(), 270, self.get_y())

        self.ln(8)

        self.set_font('helvetica', 'B', 8)
        self.cell(260/6, None, 'Payment Method', align = 'C')
        self.cell(260/6, None, 'Acount Number', align = 'C')
        self.cell(260/6, None, 'Sub-Object Code', align = 'C')
        self.cell(260/6, None, 'Project Code', align = 'C')
        self.cell(260/6, None, 'Percent', align = 'C')
        self.cell(260/6, None, 'Amount', align = 'C')

        self.ln(5)

        self.set_font('helvetica', '', 8)
        self.cell(260/6, None, 'Account', align = 'C')
        self.cell(260/6, None, account, align = 'C')
        self.cell(260/6, None, 'N/A', align = 'C')
        self.cell(260/6, None, 'N/A', align = 'C')
        self.cell(260/6, None, '100.00%', align = 'C')
        self.cell(260/6, None, f'${sum([x[3] for x in charges]):.2f}', align = 'C')

        self.output(number+'.pdf')


class quote(FPDF):

    def __init__(self):
        super().__init__(orientation = 'landscape', format = 'letter')

    def header(self):
        self.set_font('helvetica', 'B', 14)
        header_text = 'Institute for Quantitative Health Science and Engineering (IQ)'
        self.cell(self.get_string_width(header_text), None, header_text, align = 'L')
        self.set_font('helvetica', 'B', 35)
        self.set_text_color(175, 175, 175)
        self.cell(0, 25, "QUOTE", align = 'C')
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

    def generate_quote(self, details, charges):
        customer, lab = details

        self.add_page()
        self.set_font('helvetica', 'B', 10)
        self.cell(30, None, 'Prepared for:', align = 'L')
        self.cell(190, None, 'Date:', align = 'R')
        self.set_font('helvetica', '', 10)
        self.cell(0, None, str(date.today()), align = 'R')
        self.ln(5)
        self.cell(30, None, f'{customer} ({lab} Lab)', align = 'L')
        self.set_font('helvetica', 'B', 10)
        self.cell(190, None, 'Customer:', align = 'R')
        self.set_font('helvetica', '', 10)
        self.cell(0, None, customer, align = 'R')

        self.ln(15)

        self.set_font('helvetica', 'B', 10)
        self.cell(260/4, None, 'Description', align = 'C')
        self.cell(260/4, None, 'Rate', align = 'C')
        self.cell(260/4, None, 'Quantity', align = 'C')
        self.cell(260/4, None, 'Charge', align = 'C')

        self.ln(6)

        self.set_font('helvetica', '', 10)
        
        for i, item in enumerate(charges):
            if charges[i][2] != 0:
                self.cell(260/4, 5, charges[i][0], align = 'L', border = True)
                self.cell(260/4, 5, f'${charges[i][1]:.2f}', align = 'C', border = True)
                self.cell(260/4, 5, f'{charges[i][2]:.2f}', align = 'C', border = True)
                self.cell(260/4, 5, f'${charges[i][3]:.2f}', align = 'C', border = True)
                self.ln()

        self.ln()
        self.set_font('helvetica', 'B', 10)
        self.set_x(260/2 + 10)
        self.cell(260/4, None, 'Total:', align = 'C')
        self.cell(0, None, f'${sum([x[3] for x in charges]):.2f}', align = 'C')

        self.output(f'{customer}_quote.pdf')
