from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

class VaderSentiment:

    def __init__(self, path):
        self.path = path
        self.data = []
        self.score = []


    def read_csv(self):
        
        self.df = pd.read_csv(self.path + "\\Comments" + "\\Cleanse" + "\\All_comments_Cleanse.csv")
   
         # extract specific column
        dfs = self.df['body']
        self.dftweet = pd.DataFrame(dfs)

        dfT = self.df['timestamp']
        self.dftime = pd.DataFrame(dfT)

        return self.df

    def extract_column(self):

        self.dftweet = self.df['body']
        print(self.dftweet)

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
        df1 = pd.DataFrame(self.data)
        df2 = pd.DataFrame(self.score)
        # concat all data columns into a dataframe
        # print(self.df2)
        newdf= pd.concat([self.dftime,df1, df2] ,axis=1)

        print(newdf)


        newdf.columns=['timestamp','body','neg','neu','pos','compound']

        #add index to data frame
        newdf.index = pd.MultiIndex.from_arrays([newdf.index])
        
        newdf.to_csv(self.path + "\\Comments" + "\\Final_Senti" + "\\Reddit_comments_senti.csv")

        return newdf

# SentimentAnalysis = VaderSentiment()
# Read = SentimentAnalysis.read_csv()
# PullColumn = SentimentAnalysis.extract_column()
# Analysis = SentimentAnalysis.sentimentanalysis()



