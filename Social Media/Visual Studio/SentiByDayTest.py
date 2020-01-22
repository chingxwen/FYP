import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jiajie/Desktop/FYP/MLReadyDesktop/Sentiment Analysis/April2019CommentsSentimentAll.csv", index_col=0)

score = df["compound"]

print(type(score))

Polarity = []
for sentiment in score:
    if sentiment > 0:
        Polarity.append(1)
    elif sentiment < 0:
        Polarity.append(-1)
    else:
        Polarity.append(0)
GeneralSenti = pd.DataFrame(Polarity, columns = ["General_Sentiment"])
df = pd.concat([df, GeneralSenti], axis = 1)
print(df.head())
print(df.tail())