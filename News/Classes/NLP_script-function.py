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


#All the words in the article
article_comment_words = ''

for i in range(len(df['Text'])):
#     print(df['Text'][i])
    article_comment_words = article_comment_words + df['Text'][i] + ' '
# print(len(article_comment_words))

#All the words in the article before NLP

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate(article_comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 


#All the words in the article added into a var
comment_content_words = ''
for i in range(len(content)):
    for values in content[i]:
        comment_content_words = comment_content_words + values + ' '
#         print(values)
# print(len(comment_content_words))

#All the words in the article after NLP

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate(comment_content_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 


#All the words in the article that are identified as "JJ" added into a var
comment_words = ''
for i in range(len(net_senti)):
    for values in net_senti[i]:
        comment_words = comment_words + values[0] + ' '
# print(len(comment_words))

#Wordcloud based on the feeling words after NLP
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
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

