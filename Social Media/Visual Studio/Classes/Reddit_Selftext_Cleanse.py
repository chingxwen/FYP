import pandas as pd 
import csv
import re
import datetime as dt
import numpy as np


class redditSelfTextCleanse(object):

    datafile = input('whcih file would you like to clense: ')


    def __init__(self):
        pass

    def read_csv(self):

        self.df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/raw/' + self.datafile + '.csv')
        # print(self.df)

        return self.df

    def cleanse(self):
                
        # self.df.sort_values("id", inplace = True)
        print(self.df.shape)
        self.df.drop_duplicates(subset="id", keep="first", inplace=True)
        print(self.df.shape)
        print('duplicates removed')

        #remove duplicate rows
        self.df.drop(columns=['id'], inplace = True)
        self.df.drop(columns=['subreddit'], inplace=True)
        print('unwanted columns removed')
        

        #remove links 
        # try:
        #     self.df['selftext'].str.replace(r'http\S+|www.\S+', '', case=False)
        #     print('links removed')
        # except OSError:
        #     print("File cannot be opened")
        # except TypeError:
        #     print("File does not have any links to remove")
        # else:
        #     pass
        self.df['selftext'].str.replace(r'http\S+|www.\S+', '', case=False)
        print('links removed')


        #remove spaces
        self.dflist = self.df['selftext'].tolist()
        self.dfnewlist = []

        for x in range(len(self.dflist)):

            self.dflist[x] = " ".join(str(self.dflist[x]).split())
            self.dflist[x] = self.dflist[x].replace('\r', '').replace('\n', '')
            self.dfnewlist.append(self.dflist[x])
            # print(dflist[x])

        #convert to dataframe again
        self.df['selftext'] = pd.DataFrame(self.dfnewlist)
        

        #dropping NaN
        # dffinal = df.dropna()
        # print('NaN dropped')

        self.df['selftext'].replace('nan',np.nan,inplace=True)
        self.df['selftext'].replace('[removed]', np.nan, inplace = True)
        self.df.dropna(axis = 0, how = 'any', inplace = True) 

        print(self.df)
        return self.df

    def concat_write(self):
        self.df = pd.concat([self.df['selftext'],self.df['timestamp']], axis = 1)
        #Write out
        pd.DataFrame.from_dict(data = self.df , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/raw/Cleanse/' + self.datafile + 'Cleanse.csv')
        print('written!')
        
        return self.df

# RedditSelfTextCleanse = redditSelfTextCleanse()
# ReadFile = RedditSelfTextCleanse.read_csv()
# Cleanse = RedditSelfTextCleanse.cleanse()
# ConcatWrite = RedditSelfTextCleanse.concat_write()
