# Extracting data using APIs
# Make sure you have a twitter developer account

'''Step 1: log on to the twitter developer portal and get your:
consumer key, consumer secret password, access token,access token secret'''

''' Step 2: Execute the code below'''
import numpy as np
import tweepy
import json
import pandas as pd

# credentials
consumer_key = 'sksdifi' # replace with yours
consumer_secret = 'jejjcj' # replace with yours
access_token = 'fndnii' #replace with yours
access_token_secret = 'euuccbc' #replace with yours

# calling the API
auth = tweepy.OAuthHandler(	consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

# provide the query you want to pull the data
query = 'ABC' #replace with yours

# fetching tweets
Tweets = api.search(query,count = 10, lang = 'en',exclude = 'retweets',tweet_mode = 'extended')
