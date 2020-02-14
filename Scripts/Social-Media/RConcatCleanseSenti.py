from Class import SelfTextConcat
from Class import Reddit_Selftext_Cleanse
from Class import RedditSelfTextVaderSentimentAnlysis
from Class import CommentsConcat
from Class import Reddit_comment_cleanse
from Class import RedditCommentVaderSentimentAnlysis

path = input("Please input the filepath for the files to be downloaded to: ")

#SelfText Concat
SelfConcat = SelfTextConcat.concat(path)
SelfConcat.read_csv()
SelfConcat.combine()

#Cleanse Reddit selftext Data 
RedditSelfText_Cleanse = Reddit_Selftext_Cleanse.redditSelfTextCleanse(path)
RedditSelfText_Cleanse.read_csv()
RedditSelfText_Cleanse.cleanse()
RedditSelfText_Cleanse.concat_write()

#Self Text Senti

RedditSTsenti = RedditSelfTextVaderSentimentAnlysis.VaderSentiment(path)
RedditSTsenti.read_csv()
RedditSTsenti.extract_column()
RedditSTsenti.sentimentanalysis()

# Comment Concat 
ComConcat = CommentsConcat.concat(path)
ComConcat.read_csv()
ComConcat.combine()

# # Cleanse Reddit comment Data 
RedditExtract = Reddit_comment_cleanse.reddit_comment_cleanse(path)
RedditExtract.body_type()
RedditExtract.link_removal()
RedditExtract.datetimeObject_convert()
RedditExtract.space_removal()
RedditExtract.dataframe_convert()
RedditExtract.keyword_search()
RedditExtract.nullValue_removal()
RedditExtract.specialChar_removal()
RedditExtract.write()

# # Comment Senti 
CommentSenti = RedditCommentVaderSentimentAnlysis.VaderSentiment(path)
CommentSenti.read_csv()
CommentSenti.extract_column()
CommentSenti.sentimentanalysis()
