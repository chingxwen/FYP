from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

pd.options.display.max_rows = 999999

datafile = input('What CSV do you want to conduct analysis one? ')

df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Relevant/' + datafile +'Relevant.csv', names=["User", "Date", "Tweets"])
# df = pd.read_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/Keywords/Format/Cleanse/' + datafile +'Cleanse.csv', names=["Tweets", "Date"])

df = df['Tweets']
print(type(df))
dftweet = pd.DataFrame(df)
print(type(dftweet))
dflist = dftweet.values.tolist()
print(type(dflist))


analyser = SentimentIntensityAnalyzer()
data = []
score = []
positive = []
negative = []
neutral = []
def sentiment_analyzer_scores (sentence):
    result = analyser.polarity_scores(sentence)
    sentiment = "{:-<40}".format(sentence)

    data.append(sentiment)
    score.append(result)

    param = "{:-<40}".format(sentence) , str(result)

    if result['compound'] > 0:
        positive.append(param)
    elif result['compound'] < 0:
        negative.append(param)
    else:
        neutral.append(param)

    return(sentiment_analyzer_scores)
    
for i in range (len(dflist)):
    sentiment_analyzer_scores(str(dflist[i]))

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(score)

df3 = pd.DataFrame(positive)
df4 = pd.DataFrame(negative)
df5 = pd.DataFrame(neutral)


print(len(df3))
print(df1)
print(df2)

net = df2['neg'] - df2['pos']

netdata = pd.DataFrame(net ,columns = ['net'])
print(netdata.head(10))

# print(net.head(10))




df = pd.concat([df1, df2, netdata], axis=1)

df.drop(index= 0,columns=['compound'], inplace = True)

df.index = pd.MultiIndex.from_arrays([df.index])


print(df.head(10))


pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/'+ datafile + '/'+ datafile +'SentimentAll.csv')
pd.DataFrame.from_dict(data = df3 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + datafile + '/'+ datafile + 'SentimentPositive.csv')
pd.DataFrame.from_dict(data = df4 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + datafile + '/'+ datafile + 'SentimentNegative.csv')
pd.DataFrame.from_dict(data = df5 , orient = 'columns' ).to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/'+ datafile + '/' + datafile + 'SentimentNeutral.csv')
# print(len(df))
# pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/SentimentAnalysis/2018/'+ datafile + '/'+ datafile +'SentimentAll.csv')
# pd.DataFrame.from_dict(data = df3 , orient = 'columns' ).to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/SentimentAnalysis/2018/' + datafile + '/'+ datafile + 'SentimentPositive.csv')
# pd.DataFrame.from_dict(data = df4 , orient = 'columns' ).to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/SentimentAnalysis/2018/' + datafile + '/'+ datafile + 'SentimentNegative.csv')
# pd.DataFrame.from_dict(data = df5 , orient = 'columns' ).to_csv('C:/Users/jiajie25/Documents/GitHub/FYP/Social Media/CSV/SentimentAnalysis/2018/'+ datafile + '/' + datafile + 'SentimentNeutral.csv')


print('Wrote!')

# positive = []
# negative = []
# neutral = []
# for i in range(len(score)):
#     if int(score[i]) > 0:
#         positive.append(dflist[i])
#     elif int(score[i]) < 0:
#         negative.append(dflist[i])
#     else:
#         neutral.append(dflist[i])

# print(len(positive))
# print(len(negative))
# print(len(neutral))