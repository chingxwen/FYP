from Classes import Reddit_Selftext_Cleanse
from Classes import RedditSelfTextVaderSentimentAnlysis
from Classes import Reddit_comment_cleanse
from Classes import RedditCommentVaderSentimentAnlysis
from Classes import SelfTextConcat
from Classes import CommentsConcat

#SelfText Concat
SelfConcat = SelfTextConcat.concat()
SelfConcat.read_csv()
SelfConcat.combine()

#Cleanse Reddit selftext Data 
RedditSelfText_Cleanse = Reddit_Selftext_Cleanse.redditSelfTextCleanse()
RedditSelfText_Cleanse.read_csv()
RedditSelfText_Cleanse.cleanse()
RedditSelfText_Cleanse.concat_write()

#Self Text Senti

RedditSTsenti = RedditSelfTextVaderSentimentAnlysis.VaderSentiment()
RedditSTsenti.read_csv()
RedditSTsenti.extract_column()
RedditSTsenti.sentimentanalysis()

#Comment Concat 
ComConcat = CommentsConcat.concat()
ComConcat.read_csv()
ComConcat.combine()

#Cleanse Reddit comment Data 
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

#Comment Senti 

CommentSenti = RedditCommentVaderSentimentAnlysis.VaderSentiment()
CommentSenti.read_csv()
CommentSenti.extract_column()
CommentSenti.sentimentanalysis()
