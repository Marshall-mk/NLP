from sklearn.feature_extraction.text import CountVectorizer

text = ["I love NLP and I will learn NLP in 2month "]
Vectorizer = CountVectorizer()
#tokening
Vectorizer.fit(text)
# encode the document
vector = Vectorizer.transform(text)
#summerize and generate output
print(Vectorizer.vocabulary_)
print(vector.toarray())