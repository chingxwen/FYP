import tweepy
import pandas as pd
consumer_key = 'RHY3tK3sUrhfte8hXDmGdeOHX'
consumer_secret = '69YmZjbJgJXRrqob1h8aV6Jj3xG0XIVobKV5U2f0wCIno6VHqe'
access_token = '3149688854-oMHlxOstbWBy4SP5pOm2bYlOsmMnH0MtypdqBKL'
access_token_secret = '7HIEe2J6Tl1zucFa4uLps3NXR1fS009CNTPvs2w49KVuT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

<<<<<<< HEAD
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
=======
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

>>>>>>> 5fbbbc94cea837bbc72addebeda8529d10c1f359
    return tweets

tweeting = get_tweets("", 20000)
print(tweeting)
