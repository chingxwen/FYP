import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import csv
import re
import ast
from datetime import datetime

class UserClense:

    datafile = input('Which data file do you want to cleanse ?')

    def __init__(self):
        
        pass
        
    def read_Csv(self):

        self.df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Users/' + self.datafile + '.csv', names = ['ID','User','Tweets','Date'])

        return self.df
    
    def drop_columns(self): 
        #Drop columns 
        self.df.drop(columns=['ID'], inplace = True)

        return self.df

    def cleanse_data(self):

        #Extra rows by date

        # self.df['Date'] = pd.to_datetime(self.df['Date'])

        startdate = '2018-07-01'
        enddate = '2019-10-31'

        filterrows = (self.df['Date'] >= startdate) & (self.df['Date'] <= enddate)

        # self.df['Tweets'].apply(ast.literal_eval).str.decode("utf-8")

        self.df['Tweets'] = self.df['Tweets'].str.replace(r'http\S+|www.\S+', '', case=False)

        self.df['Tweets'] = self.df['Tweets'].str.replace(r'@[^\s]+','', case=False)

        self.df['Tweets'] = self.df['Tweets'].str.replace(r'[^A-Za-z0-9 ]+', '', case = False)

        # self.df['Tweets'] = self.df['Tweets'].replace('',np.nan,inplace=True)


        self.df.dropna(axis = 0, how = 'any', inplace = True)

        # Removal of Null Values
        self.df['Tweets'].replace('',np.nan,inplace=True)
        self.df['Tweets'].replace(' ',np.nan,inplace=True)
        self.df['Tweets'].replace('  ',np.nan,inplace=True)
        self.df['Tweets'].replace('   ',np.nan,inplace=True)
        self.df['Tweets'].replace('    ',np.nan,inplace=True)
        self.df.dropna(axis = 0, how = 'any', inplace = True)

        self.df['Tweets'].to_frame()
        self.df['Tweets'].tolist()

        self.df['Tweets'].str.strip().to_frame()
        # df2 = dftweet2.to_frame()


        self.df = self.df.loc[filterrows]

        print(self.df)
        print('hi')
      
        print(self.df)
        print('df')

        return self.df

    def export(self):
        # Convert list DataFrame to csv
        pd.DataFrame.from_dict(data = pd.concat([self.df['User'], self.df['Date'], self.df['Tweets']], axis = 1) , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Cleanse/' + self.datafile + 'Cleanse.csv')



#usage






