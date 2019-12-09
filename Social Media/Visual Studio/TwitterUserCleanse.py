import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import csv
import re
import ast
from googletrans import Translator
from datetime import datetime

def UserCleanse():
    datefile = input('Which data file do you want to cleanse ?')

    df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Users/' + datefile + '.csv', names = ['User','ID','Date','Tweets'])

    #Extra rows by date 
    df['Date'] = pd.to_datetime(df['Date'])

    startdate = '01-07-2018'
    enddate = '31-10-2019'

    filterrows = (df['Date'] > startdate) & (df['Date'] <= enddate)

    df = df.loc[filterrows]

    #Drop columns 
    df.drop(columns=['ID'], inplace = True)
    print(type(df))


    # remove 'b' flags
    df['Tweets'] = df['Tweets'].apply(ast.literal_eval).str.decode("utf-8")


    # remove https links
    df['Tweets'] = df['Tweets'].str.replace(r'http\S+|www.\S+', '', case=False)

    # Removal of Null Values
    df['Tweets'].replace('',np.nan,inplace=True)
    df.dropna(axis = 0, how = 'any', inplace = True)
    print(df)

    #remove username in Tweets
    df['Tweets'] = df['Tweets'].str.replace(r'@[^\s]+','', case=False)

    # Remove Special Characters 
    df['Tweets'] = df['Tweets'].str.replace(r'[^A-Za-z0-9 ]+', '', case = False)

    # Replace empty cells with Nan then Remove Empty Rows
    df['Tweets'].replace('',np.nan,inplace=True)
    df.dropna(axis = 0, how = 'any', inplace = True)

    # Removal of Null Values
    df['Tweets'].replace('',np.nan,inplace=True)
    df['Tweets'].replace(' ',np.nan,inplace=True)
    df['Tweets'].replace('  ',np.nan,inplace=True)
    df['Tweets'].replace('   ',np.nan,inplace=True)
    df['Tweets'].replace('    ',np.nan,inplace=True)
    df.dropna(axis = 0, how = 'any', inplace = True)
    print(df.head(10))

    #convert datetime to date time
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
    df['Date'] = pd.to_datetime(df['Date'])

    #Removal of Trailing White Spaces
    dfframe = df['Tweets'].to_frame()
    dflist = df['Tweets'].tolist()

    dftweet2 = df['Tweets'].str.strip()
    df2 = dftweet2.to_frame()

    final = pd.concat([df['User'], df['Date'], df['Tweets']], axis = 1)

    # Convert list DataFrame to csv
    pd.DataFrame.from_dict(data = final , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Cleanse/' + datefile + 'Cleanse.csv')

UserCleanse()