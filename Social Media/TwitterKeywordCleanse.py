import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from googletrans import Translator
import csv
import re
import ast
from aiogoogletrans import Translator
from googletrans import Translator
translator = Translator()
import asyncio
loop = asyncio.get_event_loop()


df = pd.read_csv("C:/Users/jiajie25/get_tweets/CSV/New/NewSeptember2019.csv", names=['Tweets','Date'])
translator = Translator()

# #drop extra columns
# df.drop(columns=['id', 'id_str','truncated','entities','metadata', 'source', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user','geo', 'coordinates', 'place', 'contributors', 'retweeted_status', 'is_quote_status','favorited', 'retweeted', 'extended_entities', 'possibly_sensitive', 'quoted_status_id', 'quoted_status_id_str'], inplace = True)
# # print(df)
# print('---------------------\n')
# print('Dropped\n')

#remove links
df['Tweets'] = df['Tweets'].str.replace(r'http\S+|www.\S+', '', case=False)
# print(df['text'])
print('---------------------\n')
print('Links Removed\n')

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

#Removal of Trailing White Spaces
dfframe = df['Tweets'].to_frame()
dflist = df['Tweets'].tolist()

dftweet2 = df['Tweets'].str.strip()
df2 = dftweet2.to_frame()


# #tokenize
# tokenizer = RegexpTokenizer(r'\w+')
# df['Tweets'] = df['Tweets'].apply(lambda x : tokenizer.tokenize(x))
# print(df['Tweets'])
# print('Tokenized\n')


df.to_csv('C:/Users/jiajie25/get_tweets/CSV/New/Cleanse/September2019Cleanse.csv', sep=',', index = False, header = True)


