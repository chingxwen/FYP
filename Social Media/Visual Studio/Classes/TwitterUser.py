import os
import pandas as pd
import numpy as np
import sys
import csv
import ast
import tweepy
import datetime 

class TweetMiner(object):
    
    def __init__(self, path, result_limit = 20):
            
        self.path = path
        self.result_limit = result_limit
        

    def mine_user_tweets(self,
                         mine_rewteets=False,
                         max_pages=5):

        data           =  []
        last_tweet_id  =  False
        page           =  1

        result_limit    =   20    
        data            =   []
        api             =   False
    

        self.twitter_keys = {
       'consumer_key':        'DdzX4hSW7Dth3CQb71MsTR8e2',
        'consumer_secret':     '5ZuIeoGSNODfhz7EDM9dDRT8etGXwKtHs6JtWnJDifmZq5ig8j',
        'access_token_key':    '3149688854-aby5gZg2kCGkKyoKcSP0dC2txrKipYsZsQV6e1r',
        'access_token_secret': '6f1N7oApk2RDgR7VCdAEwR4uhpRl09dEBwZpDIkZ0e1xO'
        }

        self.user = input("Enter the username without the '@' sign: ")

        auth = tweepy.OAuthHandler(self.twitter_keys['consumer_key'], self.twitter_keys['consumer_secret'])
        auth.set_access_token(self.twitter_keys['access_token_key'], self.twitter_keys['access_token_secret'])
        
        self.api = tweepy.API(auth)
        
        while page <= max_pages:
            if last_tweet_id:
                statuses   =   self.api.user_timeline(screen_name= self.user,
                                                     count=self.result_limit,
                                                     max_id=last_tweet_id - 1,
                                                     tweet_mode = 'extended',
                                                     include_retweets=True
                                                    )        
            else:
                statuses   =   self.api.user_timeline(screen_name= self.user,
                                                        count=self.result_limit,
                                                        tweet_mode = 'extended',
                                                        include_retweets=True)
                
            for item in statuses:

                mined = {
                    'User':     item.user.screen_name,
                    'Tweets':            item.full_text,
                    'Date':      item.created_at
                }
                
                last_tweet_id = item.id
                data.append(mined)
                
            page += 1
            print(data)

        outfile = self.path + "\\User" +"\\"+ self.user + ".csv"
        print(type(outfile))
        df = pd.DataFrame(data)
        print(type(df))
        df.to_csv(outfile)
        print('Written!')
    

        return data 




# TwitterExtract = TweetMiner()
# TwitterExtract.mine_user_tweets()