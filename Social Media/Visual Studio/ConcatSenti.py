from Classes import SelfTextConcat
from Classes import RedditSelfTextVaderSentimentAnlysis
from Classes import CommentsConcat
from Classes import RedditCommentVaderSentimentAnlysis

#Self Text Concat 
SelfConcat = SelfTextConcat.concat()
SelfConcat.read_csv()
SelfConcat.combine()

# Self Text Senti

RedditSTsenti = RedditSelfTextVaderSentimentAnlysis.VaderSentiment()
RedditSTsenti.read_csv()
RedditSTsenti.extract_column()
RedditSTsenti.sentimentanalysis()


#Comment Concat 
ComConcat = CommentsConcat.concat()
ComConcat.read_csv()
ComConcat.combine()

#Comment Senti 

CommentSenti = RedditCommentVaderSentimentAnlysis.VaderSentiment()
CommentSenti.read_csv()
CommentSenti.extract_column()
CommentSenti.sentimentanalysis()
