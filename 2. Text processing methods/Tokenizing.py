from textblob import TextBlob
import nltk
from nltk import word_tokenize
import pandas as pd

text=['This is introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']
df = pd.DataFrame({'tweet':text})
print(df)


#Using textblob
token = TextBlob(df['tweet'][3]).words
print(token)
#using NLTK
#create data
mystring = "My favorite animal is cat"
nltk.word_tokenize(mystring)


#using split function from python
mystring.split()