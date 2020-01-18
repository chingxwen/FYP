from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

def twitter_sentiment():
    pd.options.display.max_rows = 999999

    datafile = input('What CSV do you want to conduct analysis one? ')

    # read imported csv
    df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Relevant/' + datafile +'Relevant.csv', names=["User", "Date", "Tweets"])
    # df = pd.read_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/Keywords/Format/Cleanse/' + datafile +'Cleanse.csv', names=["Tweets", "Date"])

    # extract specific column
    dfDate = df['Date']
    df = df['Tweets']
    dftweet = pd.DataFrame(df)
    

    # convert column to list
    dflist = dftweet.values.tolist()

    # Using Vader Function to do sentiment analysis 
    analyser = SentimentIntensityAnalyzer()
    data = []
    score = []
    positive = []
    negative = []
    neutral = []

    def sentiment_analyzer_scores (sentence):
        result = analyser.polarity_scores(sentence)
        sentiment = "{:-<40}".format(sentence)

        data.append(sentiment)
        score.append(result)

        param = "{:-<40}".format(sentence) , str(result)

        #if else loop to seperate the different sentiments, negative, position and neutral
        if result['compound'] > 0:
            positive.append(param)
        elif result['compound'] < 0:
            negative.append(param)
        else:
            neutral.append(param)

        return(sentiment_analyzer_scores)
        
    # for loop to get overall sentiment analysis   
    for i in range (len(dflist)):
        sentiment_analyzer_scores(str(dflist[i]))

    #convert list to dataframes
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(score)

    df3 = pd.DataFrame(positive)
    df4 = pd.DataFrame(negative)
    df5 = pd.DataFrame(neutral)

    # Formula to calculate net sentiment
    net = df2['pos'] - df2['neg']

    # For and if else loop to determine if sentiment is Positive, Negative or Neutral
    netposneg = []

    for i in range(len(net)):

        if (net[i] > 0):

            netposneg.append('Positive')

        elif (net[i] < 0): 

            netposneg.append('Negative')

        elif (net[i] == 0):

            netposneg.append('Neutral')

    print(netposneg)

    # convert list into dataframe
    netconclude = pd.DataFrame(netposneg,columns = ['netconclude'])
    netdata = pd.DataFrame(net ,columns = ['net'])

    # concat all data columns into a dataframe
    df = pd.concat([dfDate, df1, df2, netdata,netconclude], axis=1)

    #remove unnessary columns
    df.drop(index= 0,columns=['compound'], inplace = True)

    #add index to data frame
    df.index = pd.MultiIndex.from_arrays([df.index])

    # output dataframes to csv files
    pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/'+ datafile + '/'+ datafile +'SentimentAll.csv')
    pd.DataFrame.from_dict(data = df3 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + datafile + '/'+ datafile + 'SentimentPositive.csv')
    pd.DataFrame.from_dict(data = df4 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + datafile + '/'+ datafile + 'SentimentNegative.csv')
    pd.DataFrame.from_dict(data = df5 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/'+ datafile + '/' + datafile + 'SentimentNeutral.csv')

twitter_sentiment()