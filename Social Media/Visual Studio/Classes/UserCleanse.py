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

    def __init__(self, path):
        
        self.path = path
        
    def read_Csv(self):

        #read csv
        self.df = pd.read_csv(self.path + "\\Concat" + "\\TwitterConcat.csv")

        print(self.df)
        return self.df
    
    def drop_columns(self): 
        #Drop columns 
        self.df.drop(columns=['ID'], inplace = True)

        return self.df

    def cleanse_data(self):

        #Extra rows by date

        startdate = '2018-07-01'
        enddate = '2019-10-31'

        #filter date from data
        filterrows = (self.df['Date'] >= startdate) & (self.df['Date'] <= enddate)

        #remove b flags
        self.df['Tweets'] = self.df['Tweets'].apply(ast.literal_eval).str.decode("utf-8")

        #remove links
        self.df['Tweets'] = self.df['Tweets'].str.replace(r'http\S+|www.\S+', '', case=False)

        #remove username
        self.df['Tweets'] = self.df['Tweets'].str.replace(r'@[^\s]+','', case=False)

        #remove symbols
        self.df['Tweets'] = self.df['Tweets'].str.replace(r'[^A-Za-z0-9 ]+', '', case = False)

        #drop null rows
        print(self.df)
        self.df.dropna(axis = 0, how = 'any', inplace = True)
        
        # Removal of Null Valuesss
        self.df['Tweets'].replace('',np.nan,inplace=True)
        self.df['Tweets'].replace(' ',np.nan,inplace=True)
        self.df['Tweets'].replace('  ',np.nan,inplace=True)
        self.df['Tweets'].replace('   ',np.nan,inplace=True)
        self.df['Tweets'].replace('    ',np.nan,inplace=True)
        self.df['Tweets'].dropna(axis = 0, how = 'any', inplace = True)

        self.df['Tweets'].drop_duplicates(keep="first", inplace=True)
       
        self.df['Tweets'].to_frame()
        self.df['Tweets'].tolist()

        self.df['Tweets'].str.strip().to_frame()


        self.df = self.df.loc[filterrows]
        print(self.df)


        return self.df

    def export(self):
        # Convert list DataFrame to csv
        pd.DataFrame.from_dict(data = pd.concat([self.df['User'], self.df['Date'], self.df['Tweets']], axis = 1) , orient = 'columns').to_csv(self.path + "\\Cleanse" + "\\TwitterCleanse.csv")




#usage

# TwitterCleanse = UserClense()
# TwitterCleanse.read_Csv()
# TwitterCleanse.drop_columns()
# TwitterCleanse.cleanse_data()
# TwitterCleanse.export()




