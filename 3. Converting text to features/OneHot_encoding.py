import pandas as pd
Text = 'I am learnng NLP'
vectored = pd.get_dummies(Text.split())
print(vectored)