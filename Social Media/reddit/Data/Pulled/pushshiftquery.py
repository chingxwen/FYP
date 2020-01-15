from pushshift_py import PushshiftAPI
import praw
import datetime as dt
import pandas as pd


def get_reddit():
    api = PushshiftAPI()
    reddit = praw.Reddit(
        client_id = 'ft1YI89jxATR_g', \
        client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
        user_agent = 'scrubmasterAPI', \
        username = 'pythonscrubSP', \
        password = 'scrubmaster54321'
    )

    start_epoch=int(dt.datetime(2019,10,1).timestamp())

    gen = api.search_submissions(after = start_epoch,
                                subreddit = 'samsung',
                                q = 'samsung',
                                filter = ['subreddit', 'created','title'],
                                limit = 1000)
    results = list(gen)
    print(results)



    data = pd.DataFrame(results)
    #Converting datetime column from UNIX to normal
    def get_date(created):
        return dt.datetime.fromtimestamp(created)
    _timestamp = data["created"].apply(get_date)
    data = data.assign(timestamp = _timestamp)

    #drop 'created' column
    data = data.drop('created_utc', axis = 1)

    #drop 'd_' column
    data = data.drop('d_', axis = 1)

    #drop 'created' column
    data = data.drop('created', axis = 1)

    #Write data to csv
    data.to_csv('C:/Users/jiajie/Desktop/FYP/reddit/Data/pushshiftsamsungsubmission2019October.csv', index=False)
    print('Written!')

get_reddit()