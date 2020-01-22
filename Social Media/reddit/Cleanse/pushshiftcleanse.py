import pandas as pd 
import csv
import re
import datetime as dt
import numpy as np

datafile = input('whcih file would you like to clense?')
df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/comments/' + datafile + '.csv')


#Converting datetime column from UNIX to normal
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = df["created"].apply(get_date)
df = df.assign(timestamp = _timestamp)


#remove duplicate rows
df.drop(columns=['id'], inplace = True)
df.drop(columns=['d_'], inplace = True)
df.drop(columns=['created_utc'], inplace = True)
df.drop(columns=['created'], inplace = True)
df.drop(columns=['Unnamed: 0'], inplace = True)
print(df.columns.values)

#remove links 
df['body'] = df['body'].str.replace(r'http\S+|www.\S+', '', case=False)

#convert timestamp to data time object 

df['timestamp'] = pd.to_datetime(df['timestamp'] ,format='%YY%mm%dd').dt.date

#drop null values
df['body'].replace('',np.nan,inplace=True)
df.dropna(axis = 0, how = 'any', inplace = True)

dflist = df['body'].tolist()
dfnewlist = []
#removel spaces

for x in range(len(dflist)):

    print(" ".join(dflist[x].split()))
    dfnewlist.append(dflist[x])

#convert to dataframe again

df['body'] = pd.DataFrame(dfnewlist)

df = pd.concat([df['body'],df['timestamp']], axis = 1)

#keyword search to remove automated messagede from reddit 

dict = {"*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/samsung) if you have any questions or concerns.*"
}

bodylist = df['body'].tolist()

bodycontent = df['body']
datecontent = df['timestamp']

releventbody = []
releventdate = []
count = 0

for words in dict:
    for x in range(len(bodycontent)):
        if (words in bodycontent.iloc[x]) == False:
                print(words)
                count += 1 

                # print(bodycontent.iloc[x])

                releventbody.append(bodycontent.iloc[x])
                releventdate.append(datecontent.iloc[x])

        else:
            pass

dfbody = pd.DataFrame(releventbody, columns = ['body'])
dfDate = pd.DataFrame(releventdate, columns = ['timestamp'])

df = pd.concat([dfbody, dfDate], axis = 1)

print(df)

pd.DataFrame.from_dict(data = df , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Cleanse/' + datafile + 'Cleanse.csv')
