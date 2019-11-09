import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import csv
import re
import ast

df = pd.read_csv("C:/Users/User/Desktop/FYP/Hoaxy/Hoaxy/ChannelNewsAsia.csv", names=["User", "ID", "Date", "Tweets"])

df.drop(columns=['ID'], inplace = True)

# remove 'b' flags

df['Tweets'] = df['Tweets'].apply(ast.literal_eval).str.decode("utf-8")


# remove https links

df['Tweets'] = df['Tweets'].str.replace(r'http\S+|www.\S+', '', case=False)

print(df['Tweets'].head(10))

# tokenize

tokenizer = RegexpTokenizer(r'\w+')

df['Tweets'] = df['Tweets'].apply(lambda x : tokenizer.tokenize(x))
print(df['Tweets'].head(10))

# remove stopwords
def remove_stopwords(text):
    words = [x for x in text if x not in stopwords.words('english')]
    return words

df['Tweets'] = df['Tweets'].apply(lambda x: remove_stopwords(x))

final = pd.concat(df['User'], df['ID'], df['Date'], df['Tweets'])


pd.DataFrame.from_dict(data = final , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/Hoaxy/Hoaxy/ChannelNewsAsia.csv')
