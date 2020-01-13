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

        self.df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Users/' + self.datafile + '.csv', names = ['User','ID','Date','Tweets'])

        return self.df
    
    def drop_columns(self): 
        #Drop columns 
        self.df.drop(columns=['ID'], inplace = True)

        return self.df

    def cleanse_data(self, df):

        #Extra rows by date

        df['Date'] = pd.to_datetime(df['Date'])

        startdate = '2018-07-01'
        enddate = '2019-10-31'

        filterrows = (df['Date'] >= startdate) & (df['Date'] <= enddate)

        df['Tweets'] = df['Tweets'].apply(ast.literal_eval).str.decode("utf-8")

        df['Tweets'] = df['Tweets'].str.replace(r'http\S+|www.\S+', '', case=False)

        df['Tweets'] = df['Tweets'].str.replace(r'@[^\s]+','', case=False)

        df['Tweets'] = df['Tweets'].str.replace(r'[^A-Za-z0-9 ]+', '', case = False)

        df['Tweets'].replace('',np.nan,inplace=True)
        df.dropna(axis = 0, how = 'any', inplace = True)

        # Removal of Null Values
        df['Tweets'].replace('',np.nan,inplace=True)
        df['Tweets'].replace(' ',np.nan,inplace=True)
        df['Tweets'].replace('  ',np.nan,inplace=True)
        df['Tweets'].replace('   ',np.nan,inplace=True)
        df['Tweets'].replace('    ',np.nan,inplace=True)
        df.dropna(axis = 0, how = 'any', inplace = True)

        df['Tweets'].to_frame()
        df['Tweets'].tolist()

        df['Tweets'].str.strip().to_frame()
        # df2 = dftweet2.to_frame()


        df = df.loc[filterrows]
      
        print(df)
        print('df')

        return df

    def export(self):
        # Convert list DataFrame to csv
        pd.DataFrame.from_dict(data = pd.concat([df['User'], df['Date'], df['Tweets']], axis = 1) , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Cleanse/' + self.datafile + 'Cleanse.csv')



#usage

SM_Cleanse = UserClense()
df = SM_Cleanse.read_Csv()
Date = df['Date']
Tweets = df['Tweets']
User = df['User']
SM_Drop = SM_Cleanse.drop_columns()
SM_filter = SM_Cleanse.cleanse_data(df)
SM_Cleanse.export()





