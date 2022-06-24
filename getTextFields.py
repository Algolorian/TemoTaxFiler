from PyPDF2 import PdfFileReader

location = 'D:\\Pycharm_Database\\TemoTax_Filer\\'
library_loca = location + 'Tax Publication Library\\'
temp_loca = location + 'temp\\'

pdf = PdfFileReader(temp_loca + 'fw2-2.pdf')

fields = pdf.getFormTextFields()

print(fields)
