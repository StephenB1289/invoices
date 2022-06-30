from create_pdf import invoice

pdf = invoice()
pdf.add_page()
pdf.output("invoice.pdf")