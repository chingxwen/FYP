from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

def twitter_sentiment():
    pd.options.display.max_rows = 999999

    datafile = input('What CSV do you want to conduct analysis one? ')

    # read imported csv
    dfall = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/raw/Cleanse/' + datafile +'Cleanse.csv')
    # df = pd.read_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/Keywords/Format/Cleanse/' + datafile +'Cleanse.csv', names=["Tweets", "Date"])

    # extract specific column
    df = dfall['selftext']
    dftweet = pd.DataFrame(df)

    dfT = dfall['timestamp']
    dftime = pd.DataFrame(dfT)
    # convert column to list
    dflist = dftweet.values.tolist()

    # Using Vader Function to do sentiment analysis 
    analyser = SentimentIntensityAnalyzer()
    data = []
    score = []


    def sentiment_analyzer_scores (sentence):
        result = analyser.polarity_scores(sentence)
        sentiment = "{:-<40}".format(sentence)

        data.append(sentiment)
        score.append(result)

        param = "{:-<40}".format(sentence) , str(result)

        
    # for loop to get overall sentiment analysis   
    for i in range (len(dflist)):
        sentiment_analyzer_scores(str(dflist[i]))

    #convert list to dataframes
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(score)

    # concat all data columns into a dataframe
    df = pd.concat([dftime,df1, df2], axis=1)

    df.columns=['timestamp','body','neg','neu','pos','compound']

    #add index to data frame
    # df.index = pd.MultiIndex.from_arrays([df.index])

    # output dataframes to csv files
    # pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/'+ datafile +'SentimentAll.csv')
    pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/MLReady/SelfText/'+ datafile +'SentimentAll.csv')
    # pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Sentiment Analysis/'+ datafile +'SentimentAll.csv')
 

twitter_sentiment()