import pandas as pd

datafile = input('whcih file would you like to clense?')
df = pd.read_csv("C:/FYP/Social Media/reddit/MLReady/Comments/" + datafile + 'CommentsSentimentAll.csv', index_col = 0)
print('read')
score = df['compound']

df.drop_duplicates(keep='first', inplace = True)
print('Duplicates Dropped')

#Write out
pd.DataFrame.from_dict(data = df , orient = 'columns').to_csv('C:/FYP/Social Media/reddit/MLReady/Comments/' + datafile + 'CommentsSentimentAll.csv')
print('written!')