#using skipgram
#Example sentences
sentences = [['I', 'love', 'nlp'],['I', 'will', 'learn', 'nlp', 'in', '2','months'],
['nlp', 'is', 'future'],[ 'nlp', 'saves', 'time', 'and', 'solves', 'lot', 'of', 'industry', 'problems'],
['nlp', 'uses', 'machine', 'learning']]
#import library
import gensim
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

# training the model
skipgram = Word2Vec(sentences, size =50, window = 3, min_count=1,sg = 1)
print(skipgram)
# access vector for one word
print(skipgram['nlp'])
# save model
skipgram.save('skipgram.bin')
# load model
skipgram = Word2Vec.load('skipgram.bin')
'''T – SNE plot is one of the ways to evaluate word embeddings. Let’s 
generate it and see how it looks.'''
# T – SNE plot
X = skipgram[skipgram.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(skipgram.wv.vocab)
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	pyplot.show()
