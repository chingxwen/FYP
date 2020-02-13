from Classes import Reddit_SelfText
from Classes import Reddit_comment

path = input("Please input the filepath for the files to be downloaded to: ")

# Pull reddit Data

RedditExtract = Reddit_SelfText.reddit_selftext(path)
RedditExtract.cred()
RedditExtract.extract()
RedditExtract.convert_Datetime()
RedditExtract.drop_columns()
RedditExtract.write()


#Extract Reddit Comments
RedditExtract = Reddit_comment.reddit_comments(path)
RedditExtract.extract()
RedditExtract.convert_Datetime()
RedditExtract.drop_columns()
RedditExtract.write()






