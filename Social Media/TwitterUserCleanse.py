import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import csv
import re

df = pd.read_csv("C:/Users/User/Desktop/FYP/Hoaxy/Hoaxy/ChannelNewsAsia.csv", names=["User", "ID", "Date", "Tweets"])

df.drop(columns=['ID'], inplace = True)

# remove https links
df['Tweets'] = df['Tweets'].apply(lambda x : re.sub(r'https?://\S+', '', df['Tweets'], flags=re.MULTILINE))

df['Tweets'] = df['Tweets'].str.replace('http\S+|www.\S+', '', case=False)

print(df['Tweets'].head(10))

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

# tokenize

tokenizer = RegexpTokenizer(r'\w+')

df['Tweets'] = df['Tweets'].apply(lambda x : tokenizer.tokenize(x))
print(df['Tweets'].head(10))

# remove stopwords
def remove_stopwords(text):
    words = [x for x in text if x not in stopwords.words('english')]
    return words

df['Tweets'] = df['Tweets'].apply(lambda x: remove_stopwords(x))

final = df['Tweets']

pd.DataFrame.from_dict(data = final , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/Hoaxy/Hoaxy/ChannelNewsAsia.csv')
