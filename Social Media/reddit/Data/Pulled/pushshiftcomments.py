
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
<<<<<<< HEAD
                                after = start_epoch,
                                filter = ['created','body','id'],
                                size = 1)
=======
                                q = 'samsung',
                                filter = ['subreddit', 'created','title','id'],
                                limit = 5)
>>>>>>> 67674830934446bc58ae4534df6d1803a4fbbf79
    results = list(gen)
    print('Query Done!')

    data = pd.DataFrame(results)
    print(data.head(5))    
    #Write data to csv
    data.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/pushshiftsamsungsubmission2019October.csv')
#     print('Written!')
#     print(cData)

get_redditcomments()

<<<<<<< HEAD


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
=======
    for i in range(len(iddata)):
        def listTostring(s):
            str1 = ''
            return(str1.join(s))
        print(listTostring(iddata[i]))
    cData = []
    for i in range(len(iddata)):
        try:
            x = reddit.submission(listTostring(iddata[i]))
            for comment in x.comments:
                comment = comment.body
                cData.append(comment)
                # cData.append(comment)
                # print('appended')
                # for reply in comment.replies:
                #     length = len(iddata)
                #     reply = reply.body
                #     cData.append(reply)
                #     # print('Comment Appended')
                #     # replyt = str(reply.created_utc)
                #     # cTime.append(replyt)
                #     # print('Time Appeneded')
                #     # print('\n')
                #     print(i, 'out of', length)
        except Exception as e:
            print(type(e))
            print(e)
    

    #Change to series for concat
    cData = pd.DataFrame(cData)
    # cTime = pd.DataFrame(cTime)
    # frames = [cData, cTime]
    # comdata = pd.concat(frames)
    # print(comdata)

    #Write data to csv
    cData.to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/reddit/Data/Pulled/comments/comments.csv', index=False)
    print('Written!')
    print(cData)
>>>>>>> 67674830934446bc58ae4534df6d1803a4fbbf79

    
#     data = pd.DataFrame(results)
#     data.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/commentsnew.csv')
#     print('Done!')
# get_redditcomments()