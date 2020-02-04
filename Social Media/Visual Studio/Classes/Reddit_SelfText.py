from pushshift_py import PushshiftAPI
import praw
import datetime as dt
import pandas as pd


class reddit_selftext(object):

    # api = PushshiftAPI()
    api = False
    reddit = praw.Reddit(
        client_id = 'ft1YI89jxATR_g', \
        client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
        user_agent = 'scrubmasterAPI', \
        username = 'pythonscrubSP', \
        password = 'scrubmaster54321'
    )
    print('initialised')

    yearInput = int(input('Year to Search? (YYYY):  '))
    monthInput = int(input('Month to Search? (MM):  '))
    dateInput = int(input('Date to Search? (DD):    '))

    start_epoch=int(dt.datetime(yearInput,monthInput,dateInput).timestamp())
    month = dt.date(1900, monthInput, 1).strftime('%B')
    print('Timestamp gotten')
    print('This is the time in Unix-Format:', start_epoch)
    print('You are searching in the month of '+ month)
    
    def __init__(self,api = api, keys_dict=reddit):
        self.api = PushshiftAPI()
        self.reddit = keys_dict
        self.timestamps = timestamps = []

    def extract(self):
        self.gen = self.api.search_submissions(after = self.start_epoch,
                                    subreddit = 'samsung',
                                    q = 'samsung',
                                    filter = ['subreddit', 'created','selftext','id'],
                                    limit = 500)
        self.results = list(self.gen)

        self.data = pd.DataFrame(self.results)

        return self.data

    def convert_Datetime(self):
        #Converting datetime column from UNIX to normal
        self.timelist = self.data['created'].tolist()
        for i in range(len(self.timelist)):
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

        return self.data

    def write(self):

        #Write data to csv
        # self.data.to_csv(r'C:\Users\User\Desktop\FYP\FYP\Social Media\reddit\Data\Pulled\raw\October2019.csv', index=False)
        self.data.to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/reddit/Data/Pulled/raw/' + self.month + str(self.yearInput)+'.csv', index=False)
        print('Written!')
        print(self.data.head(10))

        return self.data


# RedditExtract = reddit_selftext(object)
# RedditExtract.extract()
# RedditExtract.convert_Datetime()
# RedditExtract.drop_columns()
# RedditExtract.write()