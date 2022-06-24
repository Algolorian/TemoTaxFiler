import PyPDF2

location = 'D:\\Pycharm_Database\\TemoTax_Filer\\'
library_loca = location + 'Tax Publication Library\\'
temp_loca = location + 'temp\\'


file = open(temp_loca + 'f1040.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)


print(reader.numPages)
writer = PyPDF2.PdfFileWriter()

fields = reader.getFormTextFields()

print(fields)
i = 0
for field in fields:
    i += 1
    fields.update({field: f'0{i}'})
print(fields)

for j in range(reader.getNumPages()):
    page = reader.getPage(j)
    writer.updatePageFormFieldValues(page, fields=fields)
    writer.addPage(page)

with open(location + "newfile.pdf", "wb") as new:
    writer.write(new)





