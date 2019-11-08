import tweepy
import pandas as pd
consumer_key = 'RHY3tK3sUrhfte8hXDmGdeOHX'
consumer_secret = '69YmZjbJgJXRrqob1h8aV6Jj3xG0XIVobKV5U2f0wCIno6VHqe'
access_token = '3149688854-oMHlxOstbWBy4SP5pOm2bYlOsmMnH0MtypdqBKL'
access_token_secret = '7HIEe2J6Tl1zucFa4uLps3NXR1fS009CNTPvs2w49KVuT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

def get_tweets(query, count=300):
    q1 = str(input("Enter your keywords: "))
    a=str(q1)
    status = api.search(a, count = count )
    print("searched\n")

    df = pd.DataFrame(status['statuses'])
    print(type(df))
    print('\n')

    for tweets in status:
        print(df)
        df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/TweeterByKeyword.csv', sep=',', index = False, header = True)
    return tweets

tweeting = get_tweets("", 20000)
print(tweeting)
