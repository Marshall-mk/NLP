# Create a custom lookup dictionary
lookup_dict = {'nlp':'natural language processing', 'ur':'your', "wbu" : "what about you"}
#Create a custom function for text standardization
def text_std(input_text):
	words = input_text.split()
	new_words = []
	for word in words:
		word = re.sub(r'[^\w\s]','',word)
		if word.lower() in lookup_dict:
			word = lookup_dict[word.lower()]
			new_words.append(word)
			new_text = ''.join(new_words)
	return new_text
#Run the text_std function
text_std("I like nlp it's ur choice")