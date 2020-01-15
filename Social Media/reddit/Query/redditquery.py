import praw
import pandas as pd
import datetime as dt

#Creating Reddit instances
reddit = praw.Reddit(
    client_id = 'ft1YI89jxATR_g', \
    client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
    user_agent = 'scrubmasterAPI', \
    username = 'pythonscrubSP', \
    password = 'scrubmaster54321'
)

#Accessing Reddit Threads
subreddit = reddit.subreddits.search('samsung', limit=None)


#Dictionary Creation to append data
topic_dictionary = {
    "title" : [], \
    "id"    : [],   "url"   :[], \
    "created": [], \
    "body":[]
}

#Scrape data from Reddit and append into dictionary
for submission in subreddit:
    topic_dictionary["title"].append(submission.title)
    topic_dictionary["id"].append(submission.id)
    topic_dictionary["url"].append(submission.url)
    topic_dictionary["created"].append(submission.created)
    topic_dictionary["body"].append(submission.selftext)

#Put in Dataframe for readability
data = pd.DataFrame(topic_dictionary)

#Converting datetime and creating new column from UNIX to normal
def get_date(created):
    return dt.datetime.fromtimestamp(created)
_timestamp = data["created"].apply(get_date)
data = data.assign(timestamp = _timestamp)

#drop 'created' column
data = data.drop('created', axis = 1)
print(data)

#Write data to csv
data.to_csv('C:/Users/jiajie/Desktop/FYP/reddit/Data/samsung.csv', index=False)
print('Written!')

