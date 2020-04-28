from bs4 import BeautifulSoup
import nltk
import urllib3
from urllib.request import urlopen, Request
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

"""
# Fetch data from link provided
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = "https://wikipwedia.com"
req = Request(url=reg_url, headers=headers)
read_article = urlopen(req).read()
content_storage = BeautifulSoup.BeautifulSoup(read_article, 'html.parser')

fetchData4rmURL = urllib.request.urlopen("https://medium.com/@a20eb52bc0bc/1fb6c74bb621")
read_article = fetchData4rmURL.read()

# storing the url content as a variable
content_storage = BeautifulSoup.BeautifulSoup(read_article, 'html.parser')
"""

# link = 'https://m.wikihow.com/Pick-Up-a-Girl

link = 'https://onezero.medium.com/machine-learning-might-render-the-human-quest-for-knowledge-pointless-5425f8b00a45?source=grid_home------0------------------18---'

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
read_article = urlopen(req).read()

# storing the url content as a variable
content_storage = BeautifulSoup(read_article, 'html.parser')
# returning only paragraph tags
paragraphs = content_storage.find_all('p')
list = content_storage.find_all('li')
a = content_storage.find_all('a')

# get paragraph texts without the p tag and adding it to article content.
article_content = ' '

for para in paragraphs:
    paragraph_text = para.text
    article_content += paragraph_text

"""
for li in list:
    list_text = li.text
    article_content += list_text

for i in a:
    a_text = i.text
    article_content += a_text
"""
# Created a function to process the contents and create word frequency table

def create_freqTable(text_String) -> dict :

      stop_words = set(stopwords.words('english'))  # removing stop words
      words = word_tokenize(text_String)

      # Reduce the words to their root form
      stem = PorterStemmer()

      # creating dictionary for the word in freq table
      freq_table = dict()

      for wd in words:
          wd = stem.stem(wd)
          if wd in stop_words:
              continue
          if wd in freq_table:
              freq_table[wd] += 1
          else:
              freq_table[wd] = 1

      return freq_table


# Algo to find the weighted frequency of the sentences

def calc_weighted_freq (sentences, freq_table) -> dict:
    sentence_weights = dict()

    for sentence in sentences:
        sent_wordcount = (len(word_tokenize(sentence)))
        sent_wordcount_nonstopword = 0

        for word_weight in freq_table:
            if word_weight in sentence.lower():
                sent_wordcount_nonstopword += 1
                if sentence[:7] in sentence_weights:
                    sentence_weights[sentence[:7]] += freq_table[word_weight]
                else:
                    sentence_weights[sentence[:7]] = freq_table[word_weight]

        sentence_weights[sentence[:7]] = sentence_weights[sentence[:7]] / sent_wordcount_nonstopword

    return sentence_weights


# setting average threshold for the sentences that will appear in summary

def calc_avg_threshold(sentence_weights) -> int:
    sum_values = 0
    for entry in sentence_weights:
        sum_values += sentence_weights[entry]

    average_score = (sum_values / len(sentence_weights)) # try getting the max and min and find the average and note improvement

    return average_score

# getting the summary

def get_summary(sentences, sentence_weights, threshold):
    sentence_count = 0
    article_summary = ''

    for sentence in sentences:
         if sentence[:7] in sentence_weights and sentence_weights[sentence[:7]] >= 1.5*threshold:
             article_summary += " " + sentence + "\n"
             sentence_count += 1

    return article_summary

def run_summary_machine(article):

    freq_table = create_freqTable(article)

    # spliting the article into sentences
    sentences = sent_tokenize(article)

    weight_freq = calc_weighted_freq(sentences, freq_table)

    threshold = calc_avg_threshold(weight_freq)

    article_summary = get_summary(sentences, weight_freq, 1.2*threshold)

    return article_summary


if __name__ == '__main__':
    summary_results = run_summary_machine(article_content)
    print(summary_results)