import csv
import io
import json
import re

import pandas as pd
import tweepy
from tweepy import OAuthHandler

#TextBlob perform simple natural language processing tasks.
#from textblob import TextBlob


consumer_key = 'RHY3tK3sUrhfte8hXDmGdeOHX'
consumer_secret = '69YmZjbJgJXRrqob1h8aV6Jj3xG0XIVobKV5U2f0wCIno6VHqe'
access_token = '3149688854-oMHlxOstbWBy4SP5pOm2bYlOsmMnH0MtypdqBKL'
access_token_secret = '7HIEe2J6Tl1zucFa4uLps3NXR1fS009CNTPvs2w49KVuT'
# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)

call = input('What keywords do you wish to search for? ')

call = input('what keywords do you want to search? ')

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
def get_tweets(query, count = 1):

    # empty list to store parsed tweets
    tweets = []
    target = io.open("mytweets.txt", 'w', encoding='utf-8')
    # call twitter api to fetch tweets
    q=str(query)
    a=str(q+ call)
<<<<<<< Updated upstream
    fetched_tweets = api.search(a, count = count)
=======
    b=str(q+" sarcastic")
    c=str(q+" irony")
    fetched_tweets = api.search(a, count = count)+ api.search(b, count = count)+ api.search(c, count = count)
>>>>>>> Stashed changes
    # parsing tweets one by one
    print(len(fetched_tweets))

    for tweet in fetched_tweets:

        # empty dictionary to store required params of a tweet
        parsed_tweet = {}
        # saving text of tweet
        parsed_tweet['text'] = tweet.text
        if "http" not in tweet.text:
            line = re.sub("[^A-Za-z]", " ", tweet.text)
            target.write(line+"\n")

        tweets.append(tweet)

    return tweets

    # creating object of TwitterClient Class
    # calling function to get tweets
tweeting = get_tweets("", 1000)

print(tweeting)
df = tweeting
# print(type(tweeting))
# json_string = json.dumps(tweeting)

# df = json_string['entities']
# print(df)
##Writing to csv
pd.DataFrame.from_dict(data=df, orient='columns').to_csv("C:/Users/charmaine/Desktop/YEAR3/FYP/FYP/Social Media/Tweeting.csv", header = True)
# pd.DataFrame.from_records(tweeting , columns = tweeting).to_csv("C:\\Users\\jiajie25\\get_tweets\\Tweeting.csv", header = True, sep = ",")
# print("Written") 
