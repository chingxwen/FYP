from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

class VaderSentiment:

    datafile = input('What CSV do you want to conduct analysis on? ')
    column = input('Which column do you want to conduct analysis on?')
    pd.options.display.max_rows = 999999

    def __init__(self):
        self.data = data = []
        self.score = score = []
        self.positive = positive = []
        self.negative = negative = []
        self.neutral = neutral = []
        self.netposneg = netposneg = []
        self.net = net = 0

    def read_csv(self):

        # self.df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Relevant/' + self.datafile +'Relevant.csv', names=["User", "Date", "Tweets"])

        self.df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/pushshiftsamsungsubmission2018August.csv', names=["title", "timestamp"])
   
        return self.df

    def extract_column(self):

        self.df = self.df[self.column]
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
        df3 = pd.DataFrame(self.positive)
        df4 = pd.DataFrame(self.negative)
        df5 = pd.DataFrame(self.neutral)

    #     return self.df1, self.df2, self.df3, self.df4, self.df5

    # def calculate(self):

         # Formula to calculate net sentiment
        net = df2['pos'] - df2['neg']

        # For and if else loop to determine if sentiment is Positive, Negative or Neutral
        # netposneg = []

        for i in range(len(net)):

            if (net[i] > 0):

                self.netposneg.append('Positive')

            elif (net[i] < 0): 

                self.netposneg.append('Negative')

            elif (net[i] == 0):

                self.netposneg.append('Neutral')

            print('loop 2')

        # convert list into dataframe
        netconclude = pd.DataFrame(self.netposneg,columns = ['netconclude'])
        netdata = pd.DataFrame(net ,columns = ['net'])

        # concat all data columns into a dataframe
        df = pd.concat([df1, df2, netdata,netconclude], axis=1)

        #remove unnessary columns
        df.drop(index= 0,columns=['compound'], inplace = True)

        #add index to data frame
        df.index = pd.MultiIndex.from_arrays([df.index])

        # output dataframes to csv files
        pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/'+ self.datafile + '/'+ self.datafile +'SentimentAll.csv')
        pd.DataFrame.from_dict(data = df3 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/' + self.datafile + '/'+ self.datafile + 'SentimentPositive.csv')
        pd.DataFrame.from_dict(data = df4 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/' + self.datafile + '/'+ self.datafile + 'SentimentNegative.csv')
        pd.DataFrame.from_dict(data = df5 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/'+ self.datafile + '/' + self.datafile + 'SentimentNeutral.csv')

        
        # pd.DataFrame.from_dict(data = df3 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + self.datafile + '/'+ self.datafile + 'SentimentPositive.csv')
        # pd.DataFrame.from_dict(data = df4 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + self.datafile + '/'+ self.datafile + 'SentimentNegative.csv')
        # pd.DataFrame.from_dict(data = df5 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/'+ self.datafile + '/' + self.datafile + 'SentimentNeutral.csv')

        return df3,df4,df5 

SentimentAnalysis = VaderSentiment()
Read = SentimentAnalysis.read_csv()
PullColumn = SentimentAnalysis.extract_column()
Analysis = SentimentAnalysis.sentimentanalysis()



