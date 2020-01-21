
from pushshift_py import PushshiftAPI
import praw
import datetime as dt
import pandas as pd
from praw.models import MoreComments


def get_redditcomments():
    api = PushshiftAPI()
    reddit = praw.Reddit(
        client_id = 'ft1YI89jxATR_g', \
        client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
        user_agent = 'scrubmasterAPI', \
        username = 'pythonscrubSP', \
        password = 'scrubmaster54321'
    )

    start_epoch=int(dt.datetime(2019,10,1).timestamp())

    gen = api.search_comments(q = 'samsung',
                                subreddit = 'samsung',
                                after = start_epoch,
                                filter = ['created','body','id'],
                                size = 1)
    results = list(gen)
    print('Query Done!')

    data = pd.DataFrame(results)
    print(data.head(5))    
    #Write data to csv
    data.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/pushshiftsamsungsubmission2019October.csv')
#     print('Written!')
#     print(cData)

get_redditcomments()



# import praw
# import datetime as dt
# import pandas as pd
# from praw.models import MoreComments
# from psaw import PushshiftAPI

# def get_redditcomments():
#     api = PushshiftAPI()
#     reddit = praw.Reddit(
#         client_id = 'ft1YI89jxATR_g', \
#         client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
#         user_agent = 'scrubmasterAPI', \
#         username = 'pythonscrubSP', \
#         password = 'scrubmaster54321'
#     )

#     start_epoch=int(dt.datetime(2017, 1, 1).timestamp())

#     gen = api.search_comments(q = 'samsung',
#                               id = 'dbewaq',
#                               after = start_epoch,
#                               subreddit = 'samsung',
#                               filter=['title', 'subreddit', 'body'],
#                               limit = 10)
    
#     results = list(gen)

    
#     data = pd.DataFrame(results)
#     data.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/commentsnew.csv')
#     print('Done!')
# get_redditcomments()