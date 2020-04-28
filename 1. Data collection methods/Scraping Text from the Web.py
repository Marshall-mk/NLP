#Scraping Text from the Web

'''You want to extract data from the web by scraping. Here we have taken the 
example of the IMDB website for scraping top movies.'''

from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series, DataFrame
from ipywidgets import FloatProgress
from time import sleep
from IPython.display import display
import re
import pickle

# identify the url
url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'

# request and download content

result  = requests.get(url)
c = result.content # content of the url's response in bytes
soup = BeautifulSoup(c,'lxml')
'''Understand the website page structure to extract 
the required information'''
'''Go to the website and right-click on the page content to inspect the html 
structure of the website.
Identify the data and fields you want to extract. Say, for example, we 
want the Movie name and IMDB rating from this page.
So, we will have to check under which div or class the movie names are 
present in the HTML and parse the beautiful soup accordingly.
In the below example, to extract the movie name, we can parse 
our soup through <table class ="chart full-width">and <td 
class="titleColumn">.
Similarly, we can fetch the other details'''

'''Use beautiful soup to extract and parse 
the data from HTML tags'''
summary = soup.find('div',{'class':article})
# create empty list to append the extracted data

moviename = []
cast = []
description = []
rating = []
ratingoutof = []
year = []
genre = []
movielength = []
rot_audscore = []
rot_avgrating = []
rot_users = []

# Extracting the required data from the html soup

rgx = re.compile('[%s]'%'()')
f = FloatProgress(min=0,max=250)
display(f)
for row, i in zip(summary.find('table').findAll('tr'),range(len(summary.find('table').findAll('tr')))):
	for sitem in row.find('span',{'class':'secondaryInfo'}):
		s = sitem.find(text=True)
		year.append(rgx.sub('',s))
	for ritem in row.findAll('td',{'class':'ratingColumnimdbRating'}):
		for iget in ritem.findAll('strong'):
			rating.append(iget.find(text=True))
			ratingoutof.append(iget.get('title').split(' ',4)[3])
for item in row.findAll('td',{'class':'titleColumn'}):
	for href in item.findAll('a',href=True):
		moviename.append(href.find('a',href=True))
		rurl = ''https://www.rottentomatoes.com/m/'+ href'
		find(text=True)
		try:
			rresult = requests.get(rurl)
		except  requests.exceptions.ConnectionError:
			status_code = 'connection refused'
		rc = rresult.content
		rsoup = BeautifulSoup(rc)
		try:
			rot_audscore.append(rsoup.find('div',{'class':'meter-value'}).find('span',{'class':'superPageFontColor'}).text)
			rot_avgrating.append(rsoup.find('div',{'class':'audience-info hidden-xs superPageFontColor'}).content[3].content[2].strip())
		except AttributeError:
			rot_audscore.append('')
			rot_avgrating.append('')
			rot_users.append('')
		cast.append(href.get('title'))
		imdb = "http://www.imdb.com" + href.get('href')
		try:
			iresult = requests.get(imdb)
			ic = iresult.content
			isoup = BeautifulSoup(ic)
			description.append(isoup.find('div',{'class':'summary_text'}).find(text=True).strip())
			genre.append(isoup.find('span',{'class':'itemprop'}).find(text=True))
			movielength.append(isoup.find('time',{'itemprop':'duration'}).find(text=True).strip())
		except requests.exceptions.ConnectionError:
			description.append("")
			genre.append("")
			movielength.append("")
sleep(.1)
f.value = i

'''Converting lists to data frame and you can perform the analysis that meets the business requirement'''
# List to pandas series
moviename = Series(moviename)
cast = Series(cast)
description = Series(description)
rating = Series(rating)
ratingoutof = Series(ratingoutof)
year = Series(year)
genre = Series(genre)
movielength = Series(movielength)
rot_audscore = Series(rot_audscore)
rot_avgrating = Series(rot_avgrating)
rot_users = Series(rot_users)
# creating dataframe and doing analysis
imdb_df =  pd.concat([moviename,year,description,genre,movielength,cast,rating,ratingoutof,rot_audscore,rot_avgrating,rot_users],axis=1)
imdb_df.columns = [ 'moviename','year','description','genre','movielength','cast','imdb_rating','imdb_ratingbasedon','tomatoes_audscore','tomatoes_rating','tomatoes_ratingbasedon']
imdb_df['rank'] = imdb_df.index + 1
imdb_df.head(1)
imdb.df.to_csv("imdbdataexport.csv")
