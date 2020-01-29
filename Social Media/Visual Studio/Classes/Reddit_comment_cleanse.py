import pandas as pd 
import csv
import re
import datetime as dt
import numpy as np
import praw

class reddit_comment_cleanse(object):

    datafile = input('whcih file would you like to clense?')
    df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/comments/' + datafile + '.csv', )
    
    def __init__(self, api = api, keys_dict=reddit):
        self.api = PushshiftAPI()
    
    def body_type(self):
        self.df['body'].astype('object').dtypes
        print(self.df.dtypes.value_counts())

        return self.df['body']
    
    def link_removal(self):
        self.df['body'] = self.df['body'].str.replace(r'http\S+|www.\S+', '', case=False)

        return self.df['body']

    def datetimeObject_convert(self):
        self.df['timestamp'] = pd.to_datetime(df['timestamp'] ,format='%YY%mm%dd').dt.date
    
        return self.df['timestamp']

    self.dflist = df['body'].tolist()
    self.dfnewlist=[]

    def space_removal(self):
        for x in range(len(self.dflist)):
            self.dflist[x] = " ".join(self.dflist[x].split())
            self.dflist[x] = self.dflist[x].replace('\r', '').replace('\n', '')
            self.dfnewlist.append(self.dflist[x])
        return self.dfnewlist

    def dataframe_convert(self):
        self.df['body'] = pd.DataFrame(dfnewlist)
        self.df = pd.concat([self.df['body'],self.df['timestamp']], axis = 1)
        return self.df['body']

    def keyword_search(self):
        self.dict = {"*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/samsung) if you have any questions or concerns.*"
        }

        self.bodylist = self.df['body'].tolist()

        self.bodycontent = self.df['body'].astype(str)
        self.datecontent = self.df['timestamp']

        self.releventbody = []
        self.releventdate = []
        self.count = 0
        
        for words in self.dict:
            for x in range(len(self.bodycontent)):
                print(type(self.bodycontent.iloc[x]))
                if (words in self.bodycontent.iloc[x]) == False:
                    count += 1 

                    self.releventbody.append(bodycontent.iloc[x])
                    self.releventdate.append(datecontent.iloc[x])

                else:
                    pass

        self.dfbody = pd.DataFrame(self.releventbody, columns = ['body'])
        self.dfDate = pd.DataFrame(self.releventdate, columns = ['timestamp'])

        self.df = pd.concat([self.dfbody, self.dfDate], axis = 1)
        return self.df

    def nullValue_removal(self):
        self.df['body'].replace('',np.nan,inplace=True)
        self.df.dropna(axis = 0, how = 'any', inplace = True) 

        return self.df['body']

    def specialChar_removal(self):
        self.df['body'].str.replace("[","")
        print(self.df)

        return self.df

    def write(self):
        pd.DataFrame.from_dict(data = self.df , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Cleanse/' + datafile + 'Cleanse.csv')

        return self.df

RedditExtract = reddit_comment_cleanse(object)
RedditExtract.body_type()
RedditExtract.link_removal()
RedditExtract.datetimeObject_convert()
RedditExtract.space_removal()
RedditExtract.dataframe_convert()
RedditExtract.keyword_search()
RedditExtract.nullValue_removal()
RedditExtract.specialChar_removal()
RedditExtract.write()
