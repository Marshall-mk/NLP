# using CBOW
# training the model
cbow = Word2Vec(sentences, size =50, window = 3, min_count=1,sg = 1)
print(cbow)
# access vector for one word
print(cbow['nlp'])
# save model
cbow.save('cbow.bin')
# load model
cbow = Word2Vec.load('cbow.bin')
# T – SNE plot
X = cbow[cbow.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(cbow.wv.vocab)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	pyplot.show()

'''But to train these models, it requires a huge amount of computing 
power. So, let us go ahead and use Google’s pre-trained model, which has 
been trained with over 100 billion words.
Download the model from the below path and keep it in your local 
storage:
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
Import the gensimpackage and follow the steps to understand 
Google’s word2vec.'''

# import gensim package
import gensim
# load the saved model
model = gensim.models.Word2Vec.load_word2vec_format('C:\\Users\\GoogleNews-vectors-negative300.bin', binary=True)
#Checking how similarity works.
print (model.similarity('this', 'is'))
#Lets check one more.
print (model.similarity('post', 'book'))
# Finding the odd one out.
model.doesnt_match('breakfast cereal dinner lunch';.split())
# It is also finding the relations between words.
word_vectors.most_similar(positive=['woman', 'king'], negative=['man'])