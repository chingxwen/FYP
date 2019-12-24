from pushshift_py import PushshiftAPI
import praw
import datetime as dt


def get_reddit():
    api = PushshiftAPI()
    reddit = praw.Reddit(
        client_id = 'ft1YI89jxATR_g', \
        client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
        user_agent = 'scrubmasterAPI', \
        username = 'pythonscrubSP', \
        password = 'scrubmaster54321'
    )

    start_epoch=int(dt.datetime(2018,7,1).timestamp())

    gen = api.search_comments(after = start_epoch,
                            subreddit = 'samsung',
                            q = 'samsung',
                            limit = 2000,
                             filter = ['body'])
    results = list(gen)
    print(results)

    import pandas as pd

    data = pd.DataFrame(results)
    print(data)

    #Converting datetime column from UNIX to normal
    def get_date(created):
        return dt.datetime.fromtimestamp(created)
    _timestamp = data["created"].apply(get_date)
    data = data.assign(timestamp = _timestamp)

    print(data)

    #drop 'created' column
    data = data.drop('created_utc', axis = 1)
    print(data)

    #drop 'd_' column
    data = data.drop('d_', axis = 1)
    print(data)

    #drop 'created' column
    data = data.drop('created', axis = 1)
    print(data)

    #Write data to csv
    data.to_csv('C:/Users/jiajie/Desktop/FYP/reddit/Data/pushshiftandroid.csv', index=False)
    print('Written!')

get_reddit()