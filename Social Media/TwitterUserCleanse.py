import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import csv
import re
import ast

<<<<<<< HEAD
df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SamsungMobile.csv', names = ['User','ID','Date','Tweets'])

df.drop(columns=['ID'], inplace = True)
print(type(df))

=======
df = pd.read_csv("C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/ChannelNewsAsia.csv", names=["User", "ID", "Date", "Tweets"])

df.drop(columns=['ID'], inplace = True)
print(type(df))
>>>>>>> f285115803fab0cca4fa4e215994fdc356d47a3b
# remove 'b' flags

df['Tweets'] = df['Tweets'].apply(ast.literal_eval).str.decode("utf-8")
print(type(df['Tweets']))
# print(df['Tweets'].head(10))


# remove https links

df['Tweets'] = df['Tweets'].str.replace(r'http\S+|www.\S+', '', case=False)
print(type(df['Tweets']))
# print(df['Tweets'].head(10))

# Removal of Null Values
df['Tweets'].replace('',np.nan,inplace=True)
df.dropna(axis = 0, how = 'any', inplace = True)
print(df)

#remove username in Tweets

df['Tweets'] = df['Tweets'].str.replace(r'@[^\s]+','', case=False)

# Remove Special Characters 

df['Tweets'] = df['Tweets'].str.replace(r'[^A-Za-z0-9 ]+', '', case = False)

#Remove Empty Rows
df['Tweets'].replace('',np.nan,inplace=True)
df.dropna(axis = 0, how = 'any', inplace = True)
print(df)

print(df['Tweets'].head(10))

#remove username in Tweets

df['Tweets'] = df['Tweets'].str.replace(r'@[^\s]+','', case=False)

# Remove Special Characters 

df['Tweets'] = df['Tweets'].str.replace(r'[^A-Za-z0-9 ]+', '', case = False)


#Translate to english
dftextlist = df['Tweets'].tolist()

print('Text Read!\n')

print('Data type is: ' ,type(dftextlist))

print(len(dftextlist))


i = 0

for i in range (100):
    translated = []
    print(dftextlist[i])

    for value in translated:

        print(value.origin) 
        print('hehe')

        df = pd.DataFrame(value.origin)


<<<<<<< HEAD
# tokenizer = RegexpTokenizer(r'\w+')

# df['Text'] = df['Text'].apply(lambda x : tokenizer.tokenize(x))
# print(df['Text'].head(10))

# remove stopwords
# def remove_stopwords(text):
#     words = [x for x in text if x not in stopwords.words('english')]
#     return words

# df['Text'] = df['Text'].apply(lambda x: remove_stopwords(x))

final = pd.concat([df['User'], df['Date'], df['Tweets']], axis = 1)


pd.DataFrame.from_dict(data = final , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SamsungMobileCleanse.csv')
=======

# tokenize

# tokenizer = RegexpTokenizer(r'\w+')

# df['Tweets'] = df['Tweets'].apply(lambda x : tokenizer.tokenize(x))
# print(df['Tweets'].head(10))

# # remove stopwords
# def remove_stopwords(text):
#     words = [x for x in text if x not in stopwords.words('english')]
#     return words
    

final = pd.concat([df['User'], df['Date'], df['Tweets'] ],axis = 1)


pd.DataFrame.from_dict(data = final , orient = 'columns' ).to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/ChannelNewsAsiaCleanse.csv')
>>>>>>> f285115803fab0cca4fa4e215994fdc356d47a3b
