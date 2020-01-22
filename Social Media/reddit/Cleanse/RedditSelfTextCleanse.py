import pandas as pd 
import csv
import re
import datetime as dt
import numpy as np

datafile = input('whcih file would you like to clense?')
df = pd.read_csv('C:/FYP/Social Media/reddit/Data/Pulled/raw/' + datafile + '.csv')

df['selftext'].astype('object').dtypes

df.sort_values("id", inplace = True)
df.drop_duplicates(subset="id", keep="first", inplace=True)
print('duplicates removed')

#remove duplicate rows
df.drop(columns=['id'], inplace = True)
df.drop(columns=['subreddit'], inplace=True)
print('unwanted columns removed')

#remove links 
df['selftext'] = df['selftext'].str.replace(r'http\S+|www.\S+', '', case=False)
print('links removed')

#remove spaces
dflist = df['selftext'].tolist()
dfnewlist = []

for x in range(len(dflist)):

    dflist[x] = " ".join(dflist[x].split())
    dflist[x] = dflist[x].replace('\r', '').replace('\n', '')
    dfnewlist.append(dflist[x])
    # print(dflist[x])

#convert to dataframe again
df['selftext'] = pd.DataFrame(dfnewlist)
df = pd.concat([df['selftext'],df['timestamp']], axis = 1)

#dropping NaN
df = df.dropna()
print('NaN dropped')
print(df)

#Write out
pd.DataFrame.from_dict(data = df , orient = 'columns').to_csv('C:/FYP/Social Media/reddit/Data/Cleanse/Raw/' + datafile + 'Cleanse.csv')
print('written!')