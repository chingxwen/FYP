import GetOldTweets3 as got
import pandas as pd
number = int(input("Enter the number of data you want: "))

def getoldtweets():

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#Samsung')\
                                            .setSince("2018-12-01")\
                                            .setUntil("2018-12-31")\
                                            .setMaxTweets(number)


    get_tweets = []  
    for i in range (number):                                    
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
        get_tweets.append(tweet.text + str(tweet.date) + str (tweet.retweets))
        print('Searched!', (i+1))

    print(type(get_tweets))
    df = pd.DataFrame(get_tweets)
<<<<<<< HEAD
    df.to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/Keywords/Samsung/dec2018.csv', index=False)
=======
    csvname = input('What would you like to name ur CSV file as?')
    df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/Samsung/' + csvname + '.csv', index=False)
>>>>>>> bba18c955c35f0700d1712a7dc21507bbc88197c
    print('Written')

getoldtweets()