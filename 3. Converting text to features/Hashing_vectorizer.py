from sklearn.feature_extraction.text import HashingVectorizer
text = ["The quick brown fox jumped over the lazy dog."]
# Generate hash vectorizer matrix
# transform
Vectorizer_h = HashingVectorizer(n_features = 10)
# create the hashing vector
vector_h = Vectorizer_h.transform(text)
#summerize the vector
print(vector_h.shape)
print(vector_h.toarray()) 
#It created vector of size 10 and now this can be used for any supervised/unsupervised tasks.