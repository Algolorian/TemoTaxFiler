from PyPDF2 import PdfFileWriter, PdfFileReader

location = 'D:\\Pycharm_Database\\TemoTax_Filer\\'
library_loca = location + 'Tax Publication Library\\'
temp_loca = location + 'temp\\'


myfile = PdfFileReader(temp_loca + 'fw2-2.pdf')
first_page = myfile.getPage(1)
writer = PdfFileWriter()


fields = myfile.getFormTextFields()
print(fields)
for field in fields:
    fields.update({field: 33})
print(fields)


writer.updatePageFormFieldValues(first_page, fields=fields)
writer.addPage(first_page)

with open(location + "newfile.pdf", "wb") as new:
    writer.write(new)
