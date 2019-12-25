import pandas as pd
import numpy as np
import re
import nltk
from pprint import pprint
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#Reading of .csv file

df = pd.read_csv(r"C:\Users\charmaine\Desktop\YEAR3\FYP\NLP_Class\TheGuardianDataFinal.csv")
content = df['Text']
assert content.isnull().count() == len(content)


#Word count of each article before removal of stop words

def word_count(content):
    count = [len(content[i]) for i in range(len(content))]
    return count


#Tokenization and removal of punctuations

def tokenize(content):
    tokenizer = RegexpTokenizer(r'\w+')
    content = content.apply(lambda x: tokenizer.tokenize(x))
    return content
tokenize(content)
print(content)

#Removal of Stop Words

def remove_stopwords(text):
    set(stopwords.words('english'))
    words = [w for w in text if w not in stopwords.words('english')]
    return words
remove_stopwords(content)

#Lemmatization

def word_lemmatizer(text):
    lemmatizer = WordNetLemmatizer()

    lem_text = [lemmatizer.lemmatize(i, pos="a") for i in text]
    lem_text = [lemmatizer.lemmatize(i, pos="s") for i in text]
    lem_text = [lemmatizer.lemmatize(i, pos="v") for i in text]
    lem_text = [lemmatizer.lemmatize(i, pos="r") for i in text]
    lem_text = [lemmatizer.lemmatize(i, pos="n") for i in text]
    return lem_text

word_lemmatizer(content)

print(content[0])
content_freq = content


#Word count of each article after removal of stop words

countaft = [len(content[i]) for i in range(len(content))]
print(countaft)


#Part of Speech tagging

def nltk_pos_tag(content):
    content_tag = [nltk.pos_tag(i) for i in content]
    return content_tag

#Difference of word count before and after stop word removal in percentage, rounded off to 1dp

count_diff = []
for i in range(len(count)):
    count_diff.append(round(((count[i] - countaft[i])/count[i])*100, 1))
print(count_diff)


df.to_csv("Formatted_Data_Sentiment.csv", index = False)