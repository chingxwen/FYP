from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

class VaderSentiment:

    datafile = input('What CSV do you want to conduct analysis on? ')
    column = input('Which column do you want to conduct analysis on?')
    pd.options.display.max_rows = 2000

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
        
        # self.dfDate = self.df['timestamp']
        # self.df = self.df[self.column]
        print(self.df)
        self.dftweet = self.df['title']
        self.dfDate= self.df['timestamp']

        #convert column to list
        self.dflist = self.dftweet.values.tolist()
        self.dfDlist = self.dfDate.values.tolist()

        # return  self.dflist, self.dfDate
        
    
    # def sentimentanalysis(self):

        analyser = SentimentIntensityAnalyzer()
        
        def sentiment_analyzer_scores (sentence):
            self.result = analyser.polarity_scores(sentence)
            self.sentiment = "{:-<40}".format(sentence)

            self.data.append(self.sentiment)
            self.score.append(self.result)

            self.param = "{:-<40}".format(sentence) , str(self.result)

            #if else loop to seperate the different sentiments, negative, position and neutral
            if self.result['compound'] > 0:
                self.positive.append(self.param)
            elif self.result['compound'] < 0:
                self.negative.append(self.param)
            else:
                self.neutral.append(self.param)

            
            return(sentiment_analyzer_scores)

        for i in range (len(self.dflist)):
            sentiment_analyzer_scores(str(self.dflist[i]))

        #convert list to dataframes
        df1 = pd.DataFrame(self.data)
        df2 = pd.DataFrame(self.score)
        df3 = pd.DataFrame(self.positive)
        df4 = pd.DataFrame(self.negative)
        df5 = pd.DataFrame(self.neutral)
        
        
        net = df2['pos'] - df2['neg']


        for i in range(len(net)):

            if (net[i] > 0):

                self.netposneg.append('Positive')

            elif (net[i] < 0): 

                self.netposneg.append('Negative')

            elif (net[i] == 0):

                self.netposneg.append('Neutral')

        # convert list into dataframe
        netconclude = pd.DataFrame(self.netposneg,columns = ['netconclude'])
        netdata = pd.DataFrame(net ,columns = ['net'])
        Date = pd.DataFrame(self.dfDlist, columns = ['Date'])

        # concat all data columns into a dataframe
        self.df = pd.concat([Date,df1, df2, netdata,netconclude], axis=1)

        print(self.df)
        #remove unnessary columns
        self.df.drop(index= 0,columns=['compound'], inplace = True)

        #add index to data frame
        self.df.index = pd.MultiIndex.from_arrays([self.df.index])

        # output dataframes to csv filess
        pd.DataFrame.from_dict(data = self.df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/'+ self.datafile + '/'+ self.datafile +'SentimentAll.csv')
        pd.DataFrame.from_dict(data = df3 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/' + self.datafile + '/'+ self.datafile + 'SentimentPositive.csv')
        pd.DataFrame.from_dict(data = df4 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/' + self.datafile + '/'+ self.datafile + 'SentimentNegative.csv')
        pd.DataFrame.from_dict(data = df5 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/'+ self.datafile + '/' + self.datafile + 'SentimentNeutral.csv')

        
        # pd.DataFrame.from_dict(data = df3 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + self.datafile + '/'+ self.datafile + 'SentimentPositive.csv')
        # pd.DataFrame.from_dict(data = df4 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + self.datafile + '/'+ self.datafile + 'SentimentNegative.csv')
        # pd.DataFrame.from_dict(data = df5 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/'+ self.datafile + '/' + self.datafile + 'SentimentNeutral.csv')

        return df3,df4,df5,#self.dfDate

SentimentAnalysis = VaderSentiment()
Read = SentimentAnalysis.read_csv()
PullColumn = SentimentAnalysis.extract_column()
# Analysis = SentimentAnalysis.sentimentanalysis()



