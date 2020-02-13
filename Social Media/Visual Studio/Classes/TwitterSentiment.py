from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

class VaderSentiment():

    pd.options.display.max_rows = 999999

    def __init__(self, path):
        self.data = []
        self.score = []
        self.positive = []
        self.negative = []
        self.neutral = []
        self.path = path

    def read_csv(self):

        # self.df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Relevant/' + self.datafile +'Relevant.csv', names=["User", "Date", "Tweets"])

        self.df = pd.read_csv(self.path + "\\KeywordSearch" + "\\TwitterKeyword.csv")
   
        return self.df

    def extract_column(self):

        self.df = self.df['Tweets']
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

            #if else loop to seperate the different sentiments, negative, position and neutral
            if result['compound'] > 0:
                self.positive.append(self.param)
            elif result['compound'] < 0:
                self.negative.append(self.param)
            else:
                self.neutral.append(self.param)

            print(self.positive)
            return(sentiment_analyzer_scores)

        for i in range (len(self.dflist)):
            sentiment_analyzer_scores(str(self.dflist[i]))
            print('loop1')

    #     return sentiment_analyzer_scores

    # def convert_tolist(self):

        #convert list to dataframes
        df1 = pd.DataFrame(self.data)
        df2 = pd.DataFrame(self.score)


        # concat all data columns into a dataframe
        df = pd.concat([df1, df2], axis=1)

        #add index to data frame
        df.index = pd.MultiIndex.from_arrays([df.index])

        # output dataframes to csv files
        pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv(self.path + "\\Senti" + "\\Twitter_Senti.csv")

        return df

# SentimentAnalysis = VaderSentiment()
# Read = SentimentAnalysis.read_csv()
# PullColumn = SentimentAnalysis.extract_column()
# Analysis = SentimentAnalysis.sentimentanalysis()



