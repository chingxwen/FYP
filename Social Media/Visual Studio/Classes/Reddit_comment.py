from pushshift_py import PushshiftAPI
import praw
import datetime as dt
import pandas as pd


class reddit_comments(object):

    start_epoch=int(dt.datetime(2019,10,1).timestamp())
    print('Timestamp gotten')

    api = False
    reddit = praw.Reddit(
        client_id = 'ft1YI89jxATR_g', \
        client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
        user_agent = 'scrubmasterAPI', \
        username = 'pythonscrubSP', \
        password = 'scrubmaster54321'
    )

    def __init__(self, api = api, keys_dict=reddit):
        self.api = PushshiftAPI()
        self.timestamps = timestamps = []
        

    def extract(self):
        self.gen = self.api.search_comments(q = 'samsung',
                                subreddit = 'samsung',
                                after = self.start_epoch,
                                filter = ['created','body','id'],
                                size = 5)
        self.results = list(self.gen)

        self.data = pd.DataFrame(self.results)

        return self.data

    def convert_Datetime(self):
        self.timelist = self.data['created'].tolist()
        for i in range(len(self.timelist)):
            unix_timestamp = float(self.timelist[i])
            
            utc_time = dt.datetime.utcfromtimestamp(unix_timestamp)
            self.timestamps.append(utc_time)
        self.data = self.data.assign(timestamp = self.timestamps)

        return self.data

    def drop_columns(self):
        self.data = self.data.drop('created_utc', axis = 1)
        self.data = self.data.drop('d_', axis = 1)
        self.data = self.data.drop('created', axis=1)
        self.data = self.data.drop('id', axis = 1)
        return self.data 

    def write(self):
        self.data.to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/reddit/Data/Pulled/comments/October2019Comments.csv')
        print('Written!')
        print(self.data.head(10))

        return self.data

RedditExtract = reddit_comments(object)
RedditExtract.extract()
RedditExtract.convert_Datetime()
RedditExtract.drop_columns()
RedditExtract.write()