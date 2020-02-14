from pushshift_py import PushshiftAPI
import praw
import datetime as dt
import pandas as pd


class reddit_comments():
    api = False

    #Credentials
    reddit = praw.Reddit(
        client_id = 'ft1YI89jxATR_g', \
        client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
        user_agent = 'scrubmasterAPI', \
        username = 'pythonscrubSP', \
        password = 'scrubmaster54321'
    )
    print('credentials verified')

    def __init__(self, path,api = api, keys_dict=reddit):
        self.api = PushshiftAPI()
        self.timestamps =  []

        self.path = path
        print('initialised')
        
    def extract(self):

        #Input for Year/Month/Day
        self.yearInput = int(input('Year to Search? (YYYY):  '))
        monthInput = int(input('Month to Search? (MM):  '))
        dateInput = int(input('Date to Search? (DD):    '))
        print(self.yearInput, monthInput, dateInput)
        start_epoch=int(dt.datetime(self.yearInput,monthInput,dateInput).timestamp())
        self.month = dt.date(1900, monthInput, 1).strftime('%B')
        print('Timestamp gotten')
        print('This is the time in Unix-Format:', start_epoch)
        print('You are searching in the month of '+ self.month)

        #Extraction of comments
        gen = self.api.search_comments(q = 'samsung',
                                subreddit = 'samsung',
                                after = start_epoch,
                                filter = ['created','body','id'],
                                size = 1)
        results = list(gen)
        print('extracted')
        self.data = pd.DataFrame(results)
        print('converted')
        return self.data

    def convert_Datetime(self):

        #Covert UNIX to datetime
        self.timelist = self.data['created'].tolist()
        for i in range(len(self.timelist)):
            unix_timestamp = float(self.timelist[i])
            utc_time = dt.datetime.utcfromtimestamp(unix_timestamp)
            self.timestamps.append(utc_time)
        self.data = self.data.assign(timestamp = self.timestamps)
        return self.data

    def drop_columns(self):

        #Drop unwanted columns 
        self.data = self.data.drop('created_utc', axis = 1)
        self.data = self.data.drop('d_', axis = 1)
        self.data = self.data.drop('created', axis=1)
        self.data = self.data.drop('id', axis = 1)
        self.data.drop_duplicates(keep="first", inplace=True)
        return self.data 

    def write(self):

        #Write to csv
        self.data.to_csv(self.path + "\\Comments" + "\\Comments" + "\\" + self.month + str(self.yearInput) +'.csv')
        print('Written!')
        print(self.data.head(10))
        return self.data

# RedditExtract = reddit_comments(object)
# RedditExtract.extract()
# RedditExtract.convert_Datetime()
# RedditExtract.drop_columns()
# RedditExtract.write()