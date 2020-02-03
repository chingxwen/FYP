from Classes import Reddit_SelfText
from Classes import Reddit_comment
from Classes import Reddit_Selftext_Cleanse
from Classes import Reddit_comment_cleanse

#Pull reddit Data
RedditExtract = Reddit_SelfText.reddit_selftext(object)
RedditExtract.extract()
RedditExtract.convert_Datetime()
RedditExtract.drop_columns()
RedditExtract.write()

#Cleanse Reddit Data 
RedditSelfText_Cleanse = Reddit_Selftext_Cleanse.redditSelfTextCleanse()
RedditSelfText_Cleanse.read_csv()
RedditSelfText_Cleanse.cleanse()
RedditSelfText_Cleanse.concat_write()

#Extract Reddit Comments
RedditExtract = Reddit_comment.reddit_comments(object)
RedditExtract.extract()
RedditExtract.convert_Datetime()
RedditExtract.drop_columns()
RedditExtract.write()

#Cleanse Reddit Data 
RedditExtract = Reddit_comment_cleanse.reddit_comment_cleanse(object)
RedditExtract.body_type()
RedditExtract.link_removal()
RedditExtract.datetimeObject_convert()
RedditExtract.space_removal()
RedditExtract.dataframe_convert()
RedditExtract.keyword_search()
RedditExtract.nullValue_removal()
RedditExtract.specialChar_removal()
RedditExtract.write()


