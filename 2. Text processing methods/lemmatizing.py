import pandas as pd
from textblob import TextBlob ,Word


text=['I like fishing','I eat fish','There are many fishes in pound', 'leaves and leaf']
df = pd.DataFrame({'tweet':text}) 
df['tweet'] = df['tweet'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
print(df['tweet'])