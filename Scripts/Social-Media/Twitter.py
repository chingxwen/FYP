from Class import TwitterUser
from Class import UserCleanse
from Class import UserKeywordSearch

path = input('Input the file directory you want to pull to ')

TwitterExtract = TwitterUser.TweetMiner(path)
TwitterExtract.mine_user_tweets()


