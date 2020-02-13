import pandas as pd 
import csv
import re
import datetime as dt
import numpy as np
import praw

class reddit_comment_cleanse(object):

    api = False
    
    
    def __init__(self, path):
        self.path = path
    
    def body_type(self):

        self.df = pd.read_csv(self.path + '\\Comments'+ '\\Concat' + '\\All_concat_comments.csv' )
        
        self.df['body'].astype('object').dtypes
        print(self.df.dtypes.value_counts())

        return self.df['body']
    
    def link_removal(self):
        self.df['body'] = self.df['body'].str.replace(r'http\S+|www.\S+', '', case=False)

        return self.df['body']

    def datetimeObject_convert(self):
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp']).dt.date
    
        return self.df['timestamp']

    def space_removal(self):
        self.dflist = self.df['body'].tolist()
        self.dfnewlist=[]

        for x in range(len(self.dflist)):
            self.dflist[x] = " ".join(self.dflist[x].split())
            self.dflist[x] = self.dflist[x].replace('\r', '').replace('\n', '')
            self.dfnewlist.append(self.dflist[x])
        return self.dfnewlist

    def dataframe_convert(self):
        self.df['body'] = pd.DataFrame(self.dfnewlist)
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
                if (words in self.bodycontent.iloc[x]) == False:
                    # global count += 1 

                    self.releventbody.append(self.bodycontent.iloc[x])
                    self.releventdate.append(self.datecontent.iloc[x])

                else:
                    pass

        self.dfbody = pd.DataFrame(self.releventbody, columns = ['body'])
        self.dfDate = pd.DataFrame(self.releventdate, columns = ['timestamp'])

        self.df = pd.concat([self.dfbody, self.dfDate], axis = 1)
        return self.df

    def nullValue_removal(self):
        self.df['body'].replace('',np.nan,inplace=True)
        self.df.dropna(axis = 0, how = 'any', inplace = True) 


        self.df.drop_duplicates(keep="first", inplace=True)
        print(self.df.shape)
        print('duplicates removed')

        return self.df['body']



    def specialChar_removal(self):
        self.df['body'].str.replace("[","")
        print(self.df)

        return self.df

    def write(self):

        self.df.to_csv(self.path + "\\Comments"+"\\Cleanse"  + "\\All_comments_Cleanse.csv")

        return self.df

# RedditExtract = reddit_comment_cleanse(object)
# RedditExtract.body_type()
# RedditExtract.link_removal()
# RedditExtract.datetimeObject_convert()
# RedditExtract.space_removal()
# RedditExtract.dataframe_convert()
# RedditExtract.keyword_search()
# RedditExtract.nullValue_removal()
# RedditExtract.specialChar_removal()
# RedditExtract.write()
