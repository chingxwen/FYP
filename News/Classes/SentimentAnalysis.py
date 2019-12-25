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


#Creating a main list of the the total articles with feeling words that contain the feeling words for the respective articles

def feeling_words(content_tag):
    total_fw = []
    for articles in content_tag:
       article_fw = []
    for words in articles:
        #Extracting adjective words only
        if words[1].startswith('JJ'):
            article_fw.append(words)
    total_fw.append(article_fw)
    return total_fw

#Mapping of the tags to match the WordNet's POS 

def penn_to_wn(tag):
    """
    Convert between the PennTreebank tags to simple Wordnet tags
    """
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None

def wordnet_tag(total_fw):
    for article in total_fw:
        for words in article:
            penn_to_wn(words[1])


#To get the sentiments based on the dictionary from WordNet that reads the phrases/sentence and returns a numerical value for the positive and -negative sentiments

def get_sentiment(word,tag):
    """ returns list of pos neg and objective score. But returns empty list if not present in senti wordnet. """

    wn_tag = penn_to_wn(tag)
    if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
        return []

    lemma = lemmatizer.lemmatize(word, pos=wn_tag)
    if not lemma:
        return []

    synsets = wn.synsets(word, pos=wn_tag)
    if not synsets:
        return []

    # Take the first sense, the most common
    synset = synsets[0]
    swn_synset = swn.senti_synset(synset.name())

    return [swn_synset.pos_score(),swn_synset.neg_score(),swn_synset.obj_score()]


#Retrieving of sentiments for all the words in each article

def article_senti(total_fw):
    net_senti = []
    for article in total_fw:
        article_senti = []
        for words in article:
            
            senti = get_sentiment(words[0], words[1])
            if len(senti) > 0:
                print([words[0], (senti[0] - senti[1])])
                article_senti.append([words[0], (senti[0] - senti[1])])
        net_senti.append(article_senti)
    
    return net_senti

#Wordcloud

def wordcloud_text():
    #Extract all text for wordcloud
    wc_text = ''
    for i in range(len(text)):
        wc_text = wc_text + text[i] + ' '
    return wc_text

def wordcloud_generator(wc_text):
    #Wordlcloud config
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white', 
                    min_font_size = 10).generate(wc_text) 
    
    #Plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    
    plt.show() 


#Final printing and to count the number of articles that are positive, negative or neutral based on the sentiment values

def article_senti_count(net_senti):
    article_senti = []
    for article in net_senti:
        sentiment = 0
        article_word_count = 0
        for senti in article:
            print(senti[0], senti[1])
            sentiment += senti[1]
            article_word_count += 1
        print("\n********************************************\nTotal Sentiment: ", sentiment)
        print("Word Count In Article: ", article_word_count, "\n********************************************")
        print("\n**********************\n NEXT ARTICLE \n**********************")
        article_senti.append(sentiment)
    # return article_senti

    pos_art = 0
    neg_art = 0
    sentiment = []

    for senti in article_senti:
        if senti > 0:
            pos_art += 1
            sentiment.append("Positive")
        elif senti < 0:
            neg_art += 1
            sentiment.append("Negative")
        else:
            sentiment.append("Neutral")
    print("Out Of {} Articles, {} Are Positive , {} Are Negative And {} Is/Are Neutral"
        .format(len(article_senti), pos_art, neg_art, (len(article_senti) - pos_art - neg_art)))
    print(sentiment)


df['Sentiment'] = article_senti
df['Final Sentiment'] = sentiment


df.to_csv("Formatted_Data_Sentiment.csv", index = False)