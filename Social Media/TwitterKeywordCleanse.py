import pandas as pd
import numpy as numpy
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from googletrans import Translator
import csv
import re
import ast
from aiogoogletrans import Translator
from googletrans import Translator
translator = Translator()
import asyncio
loop = asyncio.get_event_loop()


df = pd.read_csv("C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/TweeterByKeyword.csv")
translator = Translator()

#drop extra columns
df.drop(columns=['id', 'id_str','truncated','entities','metadata', 'source', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user','geo', 'coordinates', 'place', 'contributors', 'retweeted_status', 'is_quote_status','favorited', 'retweeted', 'extended_entities', 'possibly_sensitive', 'quoted_status_id', 'quoted_status_id_str'], inplace = True)
# print(df)
print('---------------------\n')
print('Dropped\n')

#remove links
df['text'] = df['text'].str.replace(r'http\S+|www.\S+', '', case=False)
# print(df['text'])
print('---------------------\n')
print('Links Removed\n')

#tokenize
tokenizer = RegexpTokenizer(r'\w+')
df['text'] = df['text'].apply(lambda x : tokenizer.tokenize(x))
print(df['text'])
print('Tokenized\n')

#Translate to english
dftextlist = df['text'].tolist()
print('---------------------\n')
print('Text Read!\n')
print('---------------------\n')
print('Data type is: ' ,type(dftextlist))
print('---------------------\n')
print(len(dftextlist))
print('---------------------\n')

i = 0

for i in range (100):
    translated = []
    print(dftextlist[i])

    for value in translated:

        print(value.origin) 
        print('hehe')

        df = pd.DataFrame(value.origin)

df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Translate.csv', sep=',', index = False, header = True)


    # translated.append(translator.translate(dftextlist[i], dest='en'))
    


# print(len(text))

# translated = (translator.translate(text[0]))

# for object in translated:
#     print(object.text)
#     print('Translated\n')


# print(loop.run_until_complete(translator.translate(text)))





# #remove stopwords
# def remove_stopwords(text):
#     words = [x for x in text if x not in stopwords.words('english')]
#     return words

# df['text'] = df['text'].apply(lambda x: remove_stopwords(x))
# print(df['text'])
# print('Stopwords Removed\n')

# #write back to csv file
# pd.DataFrame.from_dict(data = df , orient = 'columns' ).to_csv('C:\\Users\\jiajie25\\get_tweets\\TwitterKeywordCleansed.csv')
# print('Cleansed\nWritten')


#Translate data
# dftext = df['text']
# print(type(dftext))
# trans = df.values.tolist()
# print(trans)

# translations = translator.translate(trans, dest='en')

# print(translations)


# df['English'] = dftext.apply(translator.translate, src='ko', dest='en').apply(getattr, args=('text',))
# translations = translator.translate(trans, dest='en')
# print(translations)