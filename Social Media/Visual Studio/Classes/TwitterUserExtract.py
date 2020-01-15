import os
import sys
import csv
import tweepy


class TwitterUserExtract:

    username = input("Enter the username without the '@' sign: ")

    tweets_for_csv = []
    tweet_count = 0

    twitter_keys = {
        'consumer_key':        'DdzX4hSW7Dth3CQb71MsTR8e2',
        'consumer_secret':     '5ZuIeoGSNODfhz7EDM9dDRT8etGXwKtHs6JtWnJDifmZq5ig8j',
        'access_token_key':    '3149688854-aby5gZg2kCGkKyoKcSP0dC2txrKipYsZsQV6e1r',
        'access_token_secret': '6f1N7oApk2RDgR7VCdAEwR4uhpRl09dEBwZpDIkZ0e1xO'
    }

    def __init__(selfkeys_dict=twitter_keys, api=api, result_limit = 100000):
        
        # self.consumer_key = consumer_key
        # self.consumer_secret = consumer_secret
        # self.access_key = access_key
        # self.access_secret = access_secret
        # self.number_of_tweets = number_of_tweets

        self.twitter_keys = keys_dict

        auth = tweepy.OAuthHandler(keys_dict['consumer_key'], keys_dict['consumer_secret'])
	    auth.set_access_token(keys_dict['access_token_key'], keys_dict['access_token_secret'])

	    self.api = tweepy.API(auth)

        self.result_limit = result_limit
        

    def get_tweets(self):

        for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
            #create array of tweet information: username, tweet id, date/time, text
            tweet_count += 1
            tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])
            print("Appended {} / {}".format(tweet_count, number_of_tweets))


    def export(self):

        #write to a new csv file from the array of tweets
        outfile = 'C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Users/' + self.username + ".csv"
        print(type(outfile))
        print ("writing to " + outfile)
        with open(outfile, 'w+') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(self.tweets_for_csv)



DataExtraction = TwitterUserExtract(
                'DdzX4hSW7Dth3CQb71MsTR8e2',
                '5ZuIeoGSNODfhz7EDM9dDRT8etGXwKtHs6JtWnJDifmZq5ig8j',
                '3149688854-aby5gZg2kCGkKyoKcSP0dC2txrKipYsZsQV6e1r',
                '6f1N7oApk2RDgR7VCdAEwR4uhpRl09dEBwZpDIkZ0e1xO',
                1000000000,

)



DataExtraction.get_tweets()
DataExtraction.export()
