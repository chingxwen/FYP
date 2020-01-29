from pushshift_py import PushshiftAPI
import praw
import datetime as dt
import pandas as pd


def reddit_commnts():

    start_epoch=int(dt.datetime(2019,10,1).timestamp())
    print('Timestamp gotten')

    
    self.reddit = praw.Reddit(
        client_id = 'ft1YI89jxATR_g', \
        client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
        user_agent = 'scrubmasterAPI', \
        username = 'pythonscrubSP', \
        password = 'scrubmaster54321'
    )

    def __init__(self, self.api=api):
        self.api = PushshiftAPI()

    def extract(self):
        self.gen = api.search_comments(q = 'samsung',
                                subreddit = 'samsung',
                                after = start_epoch,
                                filter = ['created','body','id'])
        self.results = list(self.gen)

        self.data = pd.DataFrame(self.results)

        return self.data
    
    def write(self):
        self.data.to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/reddit/Data/Pulled/comments/October2019Comments.csv')
        
        return self.data