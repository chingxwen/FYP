from pushshift_py import PushshiftAPI
import praw
import datetime as dt
import pandas as pd


class reddit_selftext(object):
    api = False

    def __init__(self,path,api = api):
        self.api = PushshiftAPI()
        self.timestamps = []
        self.path = path

    def cred(self):
        reddit = praw.Reddit(
            client_id = 'ft1YI89jxATR_g', \
            client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
            user_agent = 'scrubmasterAPI', \
            username = 'pythonscrubSP', \
            password = 'scrubmaster54321'
        )
        print('initialised')
        self.reddit = reddit
        return self.reddit

    def extract(self):
        self.yearInput = int(input('Year to Search? (YYYY):  '))
        monthInput = int(input('Month to Search? (MM):  '))
        dateInput = int(input('Date to Search? (DD):    '))
        print(self.yearInput, monthInput, dateInput)
        start_epoch=int(dt.datetime(self.yearInput,monthInput,dateInput).timestamp())
        self.month = dt.date(1900, monthInput, 1).strftime('%B')
        print('Timestamp gotten')
        print('This is the time in Unix-Format:', start_epoch)
        print('You are searching in the month of '+ self.month)
        gen = self.api.search_submissions(after = start_epoch,
                                    subreddit = 'samsung',
                                    q = 'samsung',
                                    filter = ['subreddit', 'created','selftext','id'],
                                    limit = 500)
        results = list(gen)
        self.data = pd.DataFrame(results)
        return self.data #, self.yearInput, self.month

    def convert_Datetime(self):
        #Converting datetime column from UNIX to normal
        self.data = self.data.dropna()
        self.timelist = self.data['created'].tolist()
        print(self.data.info())
        print(len(self.timelist))
        for i in range(len(self.timelist)):
            print(self.timelist[i])
            print(i)
            unix_timestamp = float(self.timelist[i])
            utc_time = dt.datetime.utcfromtimestamp(unix_timestamp)
            self.timestamps.append(utc_time)
        self.data = self.data.assign(timestamp = self.timestamps)

        return self.data

    def drop_columns(self):
        #drop 'created' column
        self.data = self.data.drop('created_utc', axis = 1)

        #drop 'd_' column
        self.data = self.data.drop('d_', axis = 1)

        #drop 'created' column
        self.data = self.data.drop('created', axis = 1)

        self.data.drop_duplicates(keep="first", inplace=True)

        return self.data

    def write(self):

        #Write data to csv
        self.data.to_csv(self.path + "\\SelfText" + "\\Pulled" + "\\" + self.month + str(self.yearInput) + '.csv', index=False)
        print('Written!')
        print(self.data.head(10))

        return self.data


