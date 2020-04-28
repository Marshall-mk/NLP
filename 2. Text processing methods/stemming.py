import nltk
from nltk.stem import PorterStemmer
import pandas as pd


text=['This is introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']
df = pd.DataFrame({'tweet':text})

st = PorterStemmer()
df = df['tweet'][:5].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))
print(df)
