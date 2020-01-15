from pushshift_py import PushshiftAPI
import praw
import datetime as dt
import pandas as pd



class get_reddit():

    reddit = praw.Reddit(
        client_id = 'ft1YI89jxATR_g', \
        client_secret = '31k1f4ORFpgtQlZ-h2QLO9qxCPc', \
        user_agent = 'scrubmasterAPI', \
        username = 'pythonscrubSP', \
        password = 'scrubmaster54321'
    )

    api = False
    start_epoch=int(dt.datetime(2018,7,1).timestamp())



    def __init__(self,keys_dict=reddit, api=api):

        self.api = PushshiftAPI()
        # self.created = created
        self.reddit = keys_dict
        self.timestamps = timestamps = []

    def redditextract(self):

        self.gen = self.api.search_comments(after = self.start_epoch,
                            subreddit = 'samsung',
                            q = 'samsung',
                            limit = 2000,
                             filter = ['body'])
        self.results = list(self.gen)
        print(self.results)

        self.data = pd.DataFrame(self.results)
        print(self.data)

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

    def dropcolumn(self):
        #drop 'created' column
        self.data = self.data.drop('created_utc', axis = 1)
        print(self.data)

        #drop 'd_' column
        self.data = self.data.drop('d_', axis = 1)
        print(self.data)

        #drop 'created' column
        self.data = self.data.drop('created', axis = 1)
        print(self.data)

        return self.data
    
    def exportcsv(self):
        self.data.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/pushshiftclass.csv', index=False)
        print('Written!')

        return self.data

Extract = get_reddit()
ExtractData = Extract.redditextract()
ConvertDate = Extract.convert_Datetime()
DropColumn = Extract.dropcolumn()
ExportCsv = Extract.exportcsv()

