import pandas as pd
#replce text with yours
text=['This is introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']

df = pd.DataFrame({'tweet':text}) #creates DataFrame
print(df)

df['tweet'] = df['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))
print(df)