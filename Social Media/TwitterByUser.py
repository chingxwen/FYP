import os
import sys
import csv
import tweepy


#Twitter API credentials
consumer_key = "DdzX4hSW7Dth3CQb71MsTR8e2"
consumer_secret = "5ZuIeoGSNODfhz7EDM9dDRT8etGXwKtHs6JtWnJDifmZq5ig8j"
access_key = "3149688854-aby5gZg2kCGkKyoKcSP0dC2txrKipYsZsQV6e1r"
access_secret = "6f1N7oApk2RDgR7VCdAEwR4uhpRl09dEBwZpDIkZ0e1xO"

#method to get a user's last tweets
def get_tweets():
	username = input("Enter the username without the '@' sign: ")
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#set count 
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
	outfile = 'C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Users/' + username + ".csv"
	print(outfile)
	print ("writing to " + outfile)
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)

get_tweets()