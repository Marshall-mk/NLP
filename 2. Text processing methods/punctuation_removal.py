import pandas as pd
#replace text with yours.
text=['This is introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']
df = pd.DataFrame({'tweet':text})
df['tweet'] = df['tweet'].str.replace('[^\w\s]','')
print(df)