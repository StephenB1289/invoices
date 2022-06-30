from invoice_template import invoice

pdf = invoice()
pdf.add_page()
pdf.output("invoice.pdf")