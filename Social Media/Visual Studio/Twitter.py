from Classes import TwitterUser
from Classes import UserCleanse
from Classes import UserKeywordSearch

TwitterExtract = TwitterUser.TweetMiner()
TwitterExtract.mine_user_tweets()

TwitterCleanse = UserCleanse.UserClense()
TwitterCleanse.read_Csv()
TwitterCleanse.drop_columns()
TwitterCleanse.cleanse_data()
TwitterCleanse.export()

TwitterCleanse = UserKeywordSearch.UserKeywordSearch()
TwitterCleanse.read_file()
TwitterCleanse.searchloop()
TwitterCleanse.export()


