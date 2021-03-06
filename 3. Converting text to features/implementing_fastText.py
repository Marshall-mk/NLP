# Import FastText
from gensim.models import FastText
from sklearn.decomposition import PCA
from matplotlib import pyplot

#Example sentences
sentences = [['I', 'love', 'nlp'],['I', 'will', 'learn', 'nlp', 'in', '2','months'],['nlp', 'is', 'future'],
[ 'nlp', 'saves', 'time', 'and', 'solves', 'lot', 'of', 'industry', 'problems'],
['nlp', 'uses', 'machine', 'learning']]
fast = FastText(sentences,size=20, window=1, min_count=1, workers=5, min_n=1, max_n=2)
# vector for word nlp
print(fast['nlp'])
print(fast['deep'])
'''This is the advantage of using fastText. The “deep” was not present in 
training of word2vec and we did not get a vector for that word. But since 
fastText is building on character level, even for the word that was not 
there in training, it will provide results. You can see the vector for the word 
“deep,” but it's not present in the input data'''
# save model
fast.save('fast.bin')
# load model
fast = Word2Vec.load('fast.bin')
# visualize
X = fast[fast.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(fast.wv.vocab)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	pyplot.show()