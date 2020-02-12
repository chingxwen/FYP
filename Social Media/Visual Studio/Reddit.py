from Classes import Reddit_SelfText
from Classes import Reddit_comment


# Pull reddit Data

RedditExtract = Reddit_SelfText.reddit_selftext(object)
RedditExtract.cred()
RedditExtract.extract()
RedditExtract.convert_Datetime()
RedditExtract.drop_columns()
RedditExtract.write()


#Extract Reddit Comments
RedditExtract = Reddit_comment.reddit_comments(object)
RedditExtract.extract()
RedditExtract.convert_Datetime()
RedditExtract.drop_columns()
RedditExtract.write()






