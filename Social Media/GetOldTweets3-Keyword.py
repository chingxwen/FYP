import GetOldTweets3 as got
import pandas as pd
number = int(input("Enter the number of data you want: "))

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('TradeWar')\
                                           .setSince("2018-07-01")\
                                           .setUntil("2018-08-31")\
                                           .setMaxTweets(number)

tweetCriteria2 = got.manager.TweetCriteria().setQuerySearch('TradeWar')\
                                           .setSince("2018-09-01")\
                                           .setUntil("2018-10-31")\
                                           .setMaxTweets(number)
                                        
tweetCriteria3 = got.manager.TweetCriteria().setQuerySearch('TradeWar')\
                                           .setSince("2018-11-01")\
                                           .setUntil("2018-12-31")\
                                           .setMaxTweets(number)

pull = [tweetCriteria, tweetCriteria2, tweetCriteria3]
get_tweets = []

i = 0 

for x in range (number):            
    tweet = got.manager.TweetManager.getTweets(pull[i])[x]
    get_tweets.append(tweet.text + str(tweet.date) + str(tweet.retweets))
    print('Searched ', (x+1))
            
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