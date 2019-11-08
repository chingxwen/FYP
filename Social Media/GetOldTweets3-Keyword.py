import GetOldTweets3 as got
import pandas as pd
number = int(input("Enter the number of data you want: "))

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('TradeWar')\
                                           .setSince("2018-07-01")\
                                           .setUntil("2018-12-31")\
                                           .setMaxTweets(number)
                                        

get_tweets = []
for i in range (number):                                           
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
    get_tweets.append(tweet.text + str(tweet.date) + str(tweet.retweets))
    print('Searched ', (i+1))
    # for object in get_tweets:
    #     textlist = []
    #     text = object.text
    #     textlist.append(text)
    #     print('Appended!')
    

##Writing to csv as pandas
print(type(get_tweets))
df = pd.DataFrame(get_tweets)
df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/keywords.csv', index=False)
print('Written')