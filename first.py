from pdf2docx import Converter
from datetime import datetime

old_pdf = 'kk.pdf'
new_doc = 'kk2023.docx'

print('start ', datetime.now())
# for i in old_pdf:
obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()
print('done')
print('end ', datetime.now())
print('finally')



