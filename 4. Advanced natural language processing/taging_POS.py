#NLTK for POS
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
Text = "I love NLP and I will learn NLP in 2 month"

stop_words = set(stopwords.words('english'))
# Tokenize the text
tokens = sent_tokenize(text)
#Generate tagging for all the tokens using loop
for i in tokens:
	words = nltk.word_tokenize(i)
	words = [w for w in words if not w in stop_words]
	# POS-tagger.
	tags = nltk.pos_tag(words)