from autocorrect import spell
from textblob import TextBlob
import pandas as pd
text=['This is introdection to NLP','It is likelly to be usefuul, to people ','Machine lerning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']
df = pd.DataFrame({'tweet':text})

df['tweet'] = df['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))


#method 1
df = df['tweet'].apply(lambda x: str(TextBlob(x).correct()))
print(df)
#method 2
print(spell(u'mussage'))
print(spell(u'sirvice'))