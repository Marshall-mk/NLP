import nltk
from nltk.corpus import stopwords
import pandas as pd

text=['This is introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']
df = pd.DataFrame({'tweet':text})
print(df)
'''Using the NLTK library, we can remove the punctuation as shown below.'''
stop = stopwords.words('english')
print(stop)
df['tweet'] =  df['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
print(df['tweet'])