# collecting data from PDFs
import PyPDF2
from PyPDF2 import PdfFileReader

# extracting the text data

with open('file.pdf','rb') as pdf:
	pdf_reader = PdfFileReader(pdf)
	print(pdf_reader.numPages)
	for page_num in range(0,20):
		page = pdf_reader.getPage(page_num)
		print(page.extractText())
	
