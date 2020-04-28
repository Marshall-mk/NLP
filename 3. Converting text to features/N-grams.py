from textblob import TextBlob
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import itertools
from nltk import bigrams
import numpy as np
Text = 'I am learnng NLP'
text = ["I love NLP and I will learn NLP in 2month "]

# using N-grams
# for unigram: use n = 1
TextBlob(Text).ngrams(1)
TextBlob(Text).ngrams(2)
TextBlob(Text).ngrams(3)
'''Bigram-based features for a document
Just like in the last recipe, we will use count vectorizer to generate features. 
Using the same function, let us generate bigram features and see what the 
output looks like.'''
Vectorizer_n = CountVectorizer(ngram_range = (2,2))
#tokenizing
Vectorizer_n.fit(text)
# encode document
vector_n = Vectorizer_n.transform(text)
# summarize & generating output
print(Vectorizer_n.vocabulary_)
print(vector_n.toarray())

#Generating Co-occurrence Matrix
def co_occurrence_matrix(corpus):
	vocab = set(corpus)
	vocab = list(vocab)
	vocab_to_index = {Word:i for i ,Word in enumerate(vocab)}
	# create bigrams from all words in corpus
	bi_grams = list(bigrams(corpus))
	#  Frequency distribution of bigrams ((word1, word2), num_occurrences)
	bigram_freq =  nltk.FreqDist(bi_grams).most_common(len(bi_grams))
	# Initialise co-occurrence matrix
	# co_occurrence_matrix[current][previous]
	co_occurrence_matrix = np.zeros((len(vocab), len(vocab)))
	# Loop through the bigrams taking the current and previous word,
	# and the number of occurrences of the bigram.
	for bigram in bigram_freq:
		current = bigram[0][1]
		previous = bigram[0][0]
		count = bigram[1]
		pos_current = vocab_to_index[current]
		pos_previous = vocab_to_index[previous]
		co_occurrence_matrix[pos_current][pos_previous] = count
	co_occurrence_matrix = np.matrix(co_occurrence_matrix)
	# return the matrix and the index
	return co_occurrence_matrix,vocab_to_index
#Generate co-occurrence matrix
#Here are the sentences for testing:
sentences = [['I', 'love', 'nlp'],['I', 'love','to' 'learn'],['nlp', 'is', 'future'],['nlp', 'is', 'cool']]
# create one list using many lists
merged = list(itertools.chain.from_iterable(sentences))
matrix = co_occurrence_matrix(merged)
# generate the matrix
CoMatrixFinal = pd.DataFrame(matrix[0], index=vocab_to_index, columns=vocab_to_index)
print(CoMatrixFinal)