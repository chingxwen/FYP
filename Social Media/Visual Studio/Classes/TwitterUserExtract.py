import json
import tweepy

api_url = input('Input your API')
consumer_key = input('Input your consumer key here')
consumer_secret = input('Input your consumer secret here')
access_key = input('Input your access key here')
access_secret = input('Input your access secret here')
number_of_tweets = input('Input the number of tweets u want to extract')

class TwitterUserExtract:

    def __init__(self, api_url,consumer_key,consumer_secret,access_key,access_secret,number_of_tweets,tweets_for_csv,tweet_count):
        
        self.api_url = api_url
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_key = access_key
        self.access_secret = access_secret
        self.number_of_tweets = number_of_tweets
        self.tweets_for_csv = []
        self.tweet_count = 0


    def get_tweets(self,api,consumer_key,consumer_secret,access_key,access_secret):

	    self.username = input("Enter the username without the '@' sign: ")
	    self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	    self.auth.set_access_token(access_key, access_secret)
	    self.api = tweepy.API(auth)

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