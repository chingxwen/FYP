import pandas
import numpy
import re
import nltk

# from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.book import *

stop_words=set(stopwords.words("english"))
print(stop_words)

data = pandas.read_csv(r'C:\Users\charmaine\Desktop\YEAR3\FYP\API Test\TheGuardian\TheGuardian.csv')
print(data.shape)
data.head(3)

count = [len(data['Text'][i]) for i in range(200)]
# print(count)

data['Count Before'] = count
# print(data)

#Tokenize
tokenizer = RegexpTokenizer(r'\w+')

data['Text'] = data['Text'].apply(lambda x: tokenizer.tokenize(x))


#Remove Stopwords
def remove_stopwords(text):
    words = [w for w in text if w not in stopwords.words('english')]
    return words

data['Text'] = data['Text'].apply(lambda x: remove_stopwords(x))


#Lemmatize
lemmatizer = WordNetLemmatizer()

def word_lemmatizer(text):
    lem_text = [lemmatizer.lemmatize(i, pos="v") for i in text]
    return lem_text

data['Text'] = data['Text'].apply(lambda x: word_lemmatizer(x))


countaft = [len(data['Text'][i]) for i in range(200)]
# print(count)
data['Count After'] = countaft

# for i in range(200):
#    freq = FreqDist(data['Text'][i])
#    freq = freq.most_common(15)
# data['Frequency Count'] = freq

freq = [FreqDist(data['Text'][i]).most_common(15) for i in range(200)]

data['Frequency Count'] = freq

# #Stem
# stemmer = PorterStemmer()

# def word_stemmer(text):
#     stem_text = [stemmer.stem(i) for i in text]
#     return stem_text

# data['Title'] = data['Title'].apply(lambda x: word_stemmer(x))

#Tag
data['Text'] = [nltk.pos_tag(i) for i in data['Text']]

data.to_csv(r'C:\Users\charmaine\Desktop\YEAR3\FYP\NLP\TheGuardian\output3.csv')