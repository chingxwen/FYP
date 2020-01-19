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

    gen = api.search_submissions(after = start_epoch,
                                subreddit = 'samsung',
                                q = 'samsung',
                                filter = ['subreddit', 'created','title','id'],
                                limit = 1000)
    results = list(gen)
    # print(results)

    #Getting post comments

    data = pd.DataFrame(results)

    iddata = data[['id']]
    iddata = iddata.values.tolist()

    for i in range(len(iddata)):
        def listTostring(s):
            str1 = ''
            return(str1.join(s))
        print(listTostring(iddata[i]))

    for i in range(len(iddata)):
        try:
            x = reddit.submission(listTostring(iddata[i]))
            for comment in x.comments:
                for reply in comment.replies:
                    length  = len(iddata)
                    cData = []
                    cData.append(reply.body)
                    print('Comment Appended!')
                    print(reply.body)
                    cTime = []
                    cTime.append(reply.created_utc)
                    print('Time Appeneded')
                    print(reply.created_utc)
                    print('\n')
                    print(i, 'out of', length)    
        except Exception as e:
            print(type(e))
            print(e)
    

    #Change to series for concat
    cData = pd.Series(cData)
    cTime = pd.Series(cTime)
    comData = pd.concat([cData, cTime])
    comData = pd.DataFrame(comData)


    #Converting datetime column from UNIX to normal
    # def get_date(created):
    #     return dt.datetime.fromtimestamp(created)
    # _timestamp = data["created"].apply(get_date)
    # data = data.assign(timestamp = _timestamp)

    # #drop columns
    # data = data.drop('created_utc', axis = 1)
    # data = data.drop('id', axis = 1)
    # data = data.drop('subreddit', axis = 1)
    # data = data.drop('title', axis=1)
    # data = data.drop('d_', axis=1)
    # data = data.drop('created', axis = 1)

    # #Assigning comments
    # data = data.assign(comments = cData)
    # data = data.assign(created = cTime)

    #Write data to csv
    comData.to_csv('C:/Users/jiajie/Desktop/FYP/reddit/Data/comments.csv', index=False, header = ['Comments', 'Time'])
    print('Written!')
    print(comData.head(5))

get_redditcomments()