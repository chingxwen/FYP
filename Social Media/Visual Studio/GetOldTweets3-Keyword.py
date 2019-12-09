import GetOldTweets3 as got
import pandas as pd
number = int(input("Enter the number of data you want: "))

def getoldtweets():

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('samsung')\
                                            .setSince("2018-10-01")\
                                            .setUntil("2018-10-31")\
                                            .setMaxTweets(number)


    get_tweets = []  
    for i in range (number):                                    
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
        get_tweets.append(tweet.text + str(tweet.date) + str (tweet.retweets))
        print('Searched!', (i+1))

    print(type(get_tweets))
    df = pd.DataFrame(get_tweets)
    df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/Samsung/October2018.csv', index=False)
    print('Written')

getoldtweets()