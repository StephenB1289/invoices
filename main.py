from invoice_template import invoice

def generate_invoice(details, charges, number):
    customer, lab, account = details
    materials, time, core = charges

    pdf = invoice()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(30, None, 'Bill to:', align = 'L')
    pdf.cell(175, None, 'Date:', align = 'R')
    pdf.output(number+'.pdf')

details = ('Stephen Branch', 'Spence', '123456')
charges = (10, 15, 20)
number = ('test')

generate_invoice(details, charges, number)