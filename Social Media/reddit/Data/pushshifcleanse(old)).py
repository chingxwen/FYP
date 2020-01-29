import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import csv
import re


#Reading of data file
# df = pd.read_csv('C:/Users/jiajie/Desktop/FYP/reddit/Data/Pulled/pushshiftsamsungsubmission2018August.csv')
df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/pushshiftsamsungsubmission2018August.csv')

#Removal of Links
df['title'] = df['title'].str.replace(r'http\S+|www.\S+', '', case=False)
print('links removed!')


# Remove Special Characters 
df['title'] = df['title'].str.replace(r'[^A-Za-z0-9 ]+', '', case = False)
print('Special Characters Removed')

#Removal of non-english words

titlelist = df['title'].tolist()
words = set(nltk.corpus.words.words())

translate = []

for i in range(len(titlelist)):

    englishonly  = " ".join(w for w in nltk.wordpunct_tokenize(titlelist[i]) \
            if w.lower() in words or not w.isalpha())
    
    translate.append(englishonly)
    
    print('success')


print(translate)
translateText = pd.DataFrame(translate)
translateTime = df['timestamp']
translateReddit = df['subreddit']

df = pd.concat([translateReddit, translateText, translateTime] , axis = 1)
# output to csv
# df.to_csv('C:/Users/jiajie/Desktop/FYP/reddit/Data/Pulled/Cleansed/pushshiftsamsungsubmission2018AugustCleansed.csv', sep=',', index = False, header = True)
df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/Cleansed/pushshiftsamsungsubmission2018AugustCleansed.csv', sep=',', index = False, header = True)

print('written!')