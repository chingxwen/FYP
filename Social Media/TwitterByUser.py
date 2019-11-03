#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import csv

#http://www.tweepy.org/
import tweepy


#Get your Twitter API credentials and enter them here
consumer_key = "RHY3tK3sUrhfte8hXDmGdeOHX"
consumer_secret = "69YmZjbJgJXRrqob1h8aV6Jj3xG0XIVobKV5U2f0wCIno6VHqe"
access_key = "3149688854-oMHlxOstbWBy4SP5pOm2bYlOsmMnH0MtypdqBKL"
access_secret = "7HIEe2J6Tl1zucFa4uLps3NXR1fS009CNTPvs2w49KVuT"

#method to get a user's last tweets
def get_tweets():
	username = input("Enter the username without the '@' sign: ")
	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler('RHY3tK3sUrhfte8hXDmGdeOHX', "69YmZjbJgJXRrqob1h8aV6Jj3xG0XIVobKV5U2f0wCIno6VHqe")
	auth.set_access_token("3149688854-oMHlxOstbWBy4SP5pOm2bYlOsmMnH0MtypdqBKL", "7HIEe2J6Tl1zucFa4uLps3NXR1fS009CNTPvs2w49KVuT")
	api = tweepy.API(auth)
	
	#set count to however many tweets you want
	number_of_tweets = 1000000000

	#get tweets
	tweets_for_csv = []
	tweet_count = 0
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        #create array of tweet information: username, tweet id, date/time, text
		tweet_count += 1
		tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])
		print("Appended {} / {}".format(tweet_count, number_of_tweets))


	#write to a new csv file from the array of tweets
	dir = os.getcwd()
	outfile = dir +  "\\" + username + ".csv"
	print(outfile)
	print ("writing to " + outfile)
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)


#if we're running this as a script
# if __name__ == '__main__':

    #get tweets for username passed at command line
    # if len(sys.argv) == 2:
    #     get_tweets(sys.argv[1])
    # else:
    #     print ("Error: enter one username")

#     # alternative method: loop through multiple users
# users = ['user1','user2']

# for user in users:
# 		get_tweets(user)
get_tweets()