# collecting data from word files

from docx import Document

doc =open('file.docx','rb')
document = docx.Document(doc)

docu = ' '
for para in document.paragraphs:
	docu +=para.text
print(docu)