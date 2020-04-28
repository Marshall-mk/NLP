# collecting data from HTML
import urllib.request  as urllib2
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Natural_language_processing'
response = urllib2.urlopen('url')
html_doc = response.read()

#parsing
soup = BeautifulSoup(html_doc,'html_parser')

strhtm = soup.prettify()
print(strhtm[:1000])

# extracting tag values
print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

#extracting all instances of a particualar tag
for x in soup.find_all('a'):
	print(x.string)

# finally the text
for x in soup.find_all('p'):
	print(x.text)


