from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

class VaderSentiment:

    pd.options.display.max_rows = 999999

    def __init__(self):
        self.data = data = []
        self.score = score = []


    def read_csv(self):

        # self.df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Relevant/' + self.datafile +'Relevant.csv', names=["User", "Date", "Tweets"])

        
        # self.df = pd.read_csv(r'C:\Users\User\Desktop\FYP\FYP\Social Media\reddit\MLReady\Comments\Concat\All_concat_comments.csv', names = ['timestamp','body','neg','neu','pos','compound'])
   

        self.df = pd.read_csv(r'C:\Users\jiajie25\Documents\GitHub\FYP\Social Media\reddit\MLReady\Comments\Concat\All_concat_comments.csv', names = ['timestamp','body','neg','neu','pos','compound'])
         # extract specific column
        dfs = self.df['body']
        dftweet = pd.DataFrame(dfs)

        dfT = self.df['timestamp']
        self.dftime = pd.DataFrame(dfT)
        # convert column to list
        dflist = dftweet.values.tolist()

        return self.df

    def extract_column(self):

        self.df = self.df['body']
        print(self.df)
        self.dftweet = pd.DataFrame(self.df)
        print(self.dftweet)

        #convert column to list
        self.dflist = self.dftweet.values.tolist()

        print(len(self.dflist))
        return  self.dflist
        
    
    def sentimentanalysis(self):

        analyser = SentimentIntensityAnalyzer()
        
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
        df = pd.concat([self.dftime,df1, df2], axis=1)


        df.columns=['timestamp','body','neg','neu','pos','compound']

        #add index to data frame
        df.index = pd.MultiIndex.from_arrays([df.index])

        # output dataframes to csv files
        # pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/'+ self.datafile + '/'+ self.datafile +'SentimentAll.csv')
        # pd.DataFrame.from_dict(data = df3 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/' + self.datafile + '/'+ self.datafile + 'SentimentPositive.csv')
        # pd.DataFrame.from_dict(data = df4 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/' + self.datafile + '/'+ self.datafile + 'SentimentNegative.csv')
        # pd.DataFrame.from_dict(data = df5 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/'+ self.datafile + '/' + self.datafile + 'SentimentNeutral.csv')

        # pd.DataFrame.from_dict(data = self.df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/MLReady/Comments/Final_Senti/Reddit_comments_senti.csv')
        
        pd.DataFrame.from_dict(data = self.df , orient = 'columns' ).to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/reddit/MLReady/Comments/Final_Senti/Reddit_comments_senti.csv')
        return df

# SentimentAnalysis = VaderSentiment()
# Read = SentimentAnalysis.read_csv()
# PullColumn = SentimentAnalysis.extract_column()
# Analysis = SentimentAnalysis.sentimentanalysis()



