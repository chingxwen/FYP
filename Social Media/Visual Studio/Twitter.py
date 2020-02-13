from Classes import TwitterUser
from Classes import UserCleanse
from Classes import UserKeywordSearch

path = input('Input the file directory you want to pull to ')

TwitterExtract = TwitterUser.TweetMiner(path)
TwitterExtract.mine_user_tweets()


