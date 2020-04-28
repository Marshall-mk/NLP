#Extract data from the ebook and perform regex
import re 
import requests

url = 'https://www.gutenberg.org/files/2638/2638-0.txt'
def get_book(url):
	raw = requests.get(url).text
	start = re.search(r'\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*',raw).end()
	stop = re.search(r'II',raw).start()
	text = raw[start:stop]
	return text

def preprocess(sentence):
	return re.sub('[^A-Za-z0-9.]+',' ',sentence).lower()

book = get_book(url)
processed_book = preprocess(book)
print(processed_book)

'''Performing some exploratory data analysis on the data'''
len(re.findall(r'the',processed_book))

processed_book = re.sub(r'\si\s','I',processed_book)
print(processed_book)

#find all occurance of text in the format "abc--xyz"
re.findall(r'[a-zA-Z0-9]*--[a-zA-Z0-9]*', book)