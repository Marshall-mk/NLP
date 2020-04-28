from sklearn.feature_extraction.text import TfidfVectorizer
Text = ["The quick brown fox jumped over the lazy dog.","The dog.","The fox"]
# creating the features
# create the features
Vectorizer_t = TfidfVectorizer()
# tokenize and build vocab
Vectorizer_t.fit(Text)
#summerize
print(Vectorizer_t.vocabulary_)
print(Vectorizer_t.idf_)
