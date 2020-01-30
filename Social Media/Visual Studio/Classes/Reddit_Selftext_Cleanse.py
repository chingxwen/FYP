import pandas as pd 
import csv
import re
import datetime as dt
import numpy as np


class RedditSelfTextCleanse(object):

    datafile = input('whcih file would you like to clense: ')


    def __init__(self):
        pass

    def read_csv(self):

        self.df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/raw/' + self.datafile + '.csv')
        # print(self.df)

        return self.df

    def cleanse(self, df):
                
        # self.df.sort_values("id", inplace = True)
        print(df.shape)
        df.drop_duplicates(subset="id", keep="first", inplace=True)
        print(df.shape)
        print('duplicates removed')

        #remove duplicate rows
        df.drop(columns=['id'], inplace = True)
        df.drop(columns=['subreddit'], inplace=True)
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
        df['selftext'].str.replace(r'http\S+|www.\S+', '', case=False)
        print('links removed')
        self.df = df

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

        print(df)
        return self.df

    def concat_write(self, df):
        df = pd.concat([df['selftext'],df['timestamp']], axis = 1)
        #Write out
        pd.DataFrame.from_dict(data = df , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Pulled/raw/Cleanse/' + self.datafile + 'Cleanse.csv')
        print('written!')
        
        self.df = df
        return self.df

RedditSelfTextCleanse = RedditSelfTextCleanse()
ReadFile = RedditSelfTextCleanse.read_csv()
Cleanse = RedditSelfTextCleanse.cleanse(ReadFile)
ConcatWrite = RedditSelfTextCleanse.concat_write(Cleanse)
print(type(Cleanse))

