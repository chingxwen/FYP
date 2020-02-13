from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

class VaderSentiment:

    def __init__(self, path):
        self.path = path
        self.data = []
        self.score = []


    def read_csv(self):

        self.df = pd.read_csv(self.path + "\\SelfText" + "\\Cleanse" + "\\All_selftext_cleanse.csv")
   
        # extract specific column
        self.dfb = self.df['title']
        dftweet = pd.DataFrame(self.dfb)

        self.dfT = self.df['timestamp']
        self.dftime = pd.DataFrame(self.dfT)

        return self.df

    def extract_column(self):

        self.df = self.df.title
        self.dftweet = pd.DataFrame(self.df)

        #convert column to list
        self.dflist = self.dftweet.values.tolist()

        return  self.dflist
        
    
    def sentimentanalysis(self):

        analyser = SentimentIntensityAnalyzer()

        pd.options.display.max_rows = 999999
        
        def sentiment_analyzer_scores (sentence):
            result = analyser.polarity_scores(sentence)
            self.sentiment = "{:-<40}".format(sentence)

            self.data.append(self.sentiment)
            self.score.append(result)

            self.param = "{:-<40}".format(sentence) , str(result)

           
        for i in range (len(self.dflist)):
            sentiment_analyzer_scores(str(self.dflist[i]))


        #convert list to dataframes
        self.df1 = pd.DataFrame(self.data)
        self.df2 = pd.DataFrame(self.score)
        # concat all data columns into a dataframe
        print(self.df1)
        print(self.df2)
        print(self.dftime)
        df = pd.concat([self.dftime,self.df1, self.df2], axis=1)

        df = df.loc[~df.index.duplicated(keep='first')]
        df = df.drop(df.index[0])

        df.columns=['timestamp','title','neg','neu','pos','compound']

        #add index to data frame
        df.index = pd.MultiIndex.from_arrays([df.index])
        
        df.to_csv(self.path + "\\SelfText" + "\\Final_Senti" + "\\Reddit_selftext_senti.csv")

        return df

# SentimentAnalysis = VaderSentiment()
# Read = SentimentAnalysis.read_csv()
# PullColumn = SentimentAnalysis.extract_column()
# Analysis = SentimentAnalysis.sentimentanalysis()



