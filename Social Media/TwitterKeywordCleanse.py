import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import csv
import re

datafile = input('Which date do you want to cleanse ? ')
df = pd.read_csv("C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/Format/New" + datafile + '.csv', names=['Tweets','Date'])

#remove links
df['Tweets'] = df['Tweets'].str.replace(r'http\S+|www.\S+', '', case=False)

# Removal of Null Values
df['Tweets'].replace('',np.nan,inplace=True)
df['Tweets'].replace(' ',np.nan,inplace=True)
df['Tweets'].replace('  ',np.nan,inplace=True)
df['Tweets'].replace('   ',np.nan,inplace=True)
df['Tweets'].replace('    ',np.nan,inplace=True)
df.dropna(axis = 0, how = 'any', inplace = True)
print(df.head(10))

# Remove Special Characters 
df['Tweets'] = df['Tweets'].str.replace(r'[^A-Za-z0-9 ]+', '', case = False)
print('Special Characters Removed')

#removal of numeric charactars
df['Tweets'] = df['Tweets'].str.replace("\\d", "")

#Removal of Trailing White Spaces
dfframe = df['Tweets'].to_frame()
dflist = df['Tweets'].tolist()

dftweet2 = df['Tweets'].str.strip()
df2 = dftweet2.to_frame()

# check for duplicate rows and remove duplicates
df.drop_duplicates(subset = 'Tweets' ,keep = 'first', inplace = True)

# output to csv
df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/Format/Cleanse/' + datafile + 'Cleanse.csv', sep=',', index = False, header = True)


