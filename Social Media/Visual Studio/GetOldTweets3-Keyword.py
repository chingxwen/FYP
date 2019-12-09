import GetOldTweets3 as got
import pandas as pd

number = int(input("Enter the number of data you want: "))

#parameters and pulling from API 

samsunglist = ["samsung","galaxy", "samsung galaxy", "samsung group", 
        "samsung technologies","galaxy s10", "galaxy note10", "galaxy fold", 
        "galaxy s10+", "galaxy s10e", "galaxy buds", "galaxy watch", "watch active 2",
        "galaxy tab", "tab S6", "galaxy book S", "samsung electronics", "samsung x IFA 2019", 
        "the wall luxury", "Q series soundbar", "seoul sisters conference", 
        " Samsung Semiconductor Institute of Technology", "galaxy A30", "galaxy S11", 
        "a70 waterproof", "a70 wireless charging", "s10 plus", "s7 edge", "galaxy m30", "galaxy j7", 
       "galaxy j2", "galaxy a10", "space zoom", "samsung support", "the serif", "#dowhatyoucant", "spacemax", 
       "galaxy A", "galaxy note", "QLED", "quickdrive", "s series", "galaxyAs", "samsung mobile", "SamsungMobileSA",
       "#DontFumbleTheBag", "galaxy a30s", "#FillUpRoyalBafokeng", "#SDC19", "galaxy buds", "samsungUS", "samsungsupport",
       "chromebook", "samsung J4", "samsung J4 core", "galaxy J4", "galaxy J2", "galaxy J4 core", "galaxy tab",
       "samsung health", "SamsungKids", "SamsungKidsUS", "samsung galacy", "TeamGalaxy", "#TeamGalaxy", "withgalaxy",
       "galaxy FIT E", "samsung T5", "galaxy T5", "Samsung Catalyst Fund", "samsungcatalyst", "SamsungCEOSummit",
       "Samsung 5G Exynos 980", "SamMobile"]

for words in samsunglist:

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(words)\
                                            .setSince("2018-08-01")\
                                            .setUntil("2018-08-31")\
                                            .setMaxTweets(number)
                                            

    get_tweets = []

    i = 0 

    for x in range (number):            
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
        get_tweets.append(tweet.text + str(tweet.date) + str(tweet.retweets))
        print('Searched ', (x+1))

    # Writing to csv 
    print(type(get_tweets))
    df = pd.DataFrame(get_tweets)
    df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/Samsung/august2018.csv', index=False)
    print('Written')