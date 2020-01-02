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
import csv


#Reading of .csv file
class class_NLP:

   filename = input("Please input the path of the CSV file: ") #r"C:\Users\charmaine\Desktop\YEAR3\FYP\FYP\News\Classes\Samsung.csv"

   def __inti__(self):
      pass

   #Read csv file
   def read_file(self):
      print("Reading csv file")
      self.data_as_csv = pd.read_csv(self.filename)
      print("There are {} column attributes: {}".format(len(self.data_as_csv.columns), list(self.data_as_csv)))
      return self.data_as_csv
      
   #Tokenization and removal of punctuations
   def tokenize(self, content):
      print("Tokenizing content")
      tokenizer = RegexpTokenizer(r'\w+')
      self.content = content.apply(lambda x: tokenizer.tokenize(x))
      print("Content is tokenized")
      return self.content

   #Removal of Stop Words
   def stopwords_removal(self):
      print("Removing stopwords")
      set(stopwords.words('english'))

      def remove_stopwords(text):
         self.words = [w for w in text if w not in stopwords.words('english')]
         return self.words

      self.content = self.content.apply(lambda x: remove_stopwords(x))
      print("Stopwords are removed")
      return self.content
   
   #Lemmatization
   def lemmatization(self):
      print("Lemmatizing content")
      lemmatizer = WordNetLemmatizer()

      def word_lemmatizer(text):
         self.lem_text = [lemmatizer.lemmatize(i, pos="a") for i in text]
         self.lem_text = [lemmatizer.lemmatize(i, pos="s") for i in text]
         self.lem_text = [lemmatizer.lemmatize(i, pos="v") for i in text]
         self.lem_text = [lemmatizer.lemmatize(i, pos="r") for i in text]
         self.lem_text = [lemmatizer.lemmatize(i, pos="n") for i in text]
         return self.lem_text

      self.content = self.content.apply(lambda x: word_lemmatizer(x))
      print("Content is lemmatized")
      return self.content

   #Part of Speech tagging
   def nltk_pos_tag(self):
      print("Tagging words")
      self.content = [nltk.pos_tag(i) for i in self.content]
      print("Words are tagged")
      return self.content

News_NLP = class_NLP()
df = News_NLP.read_file()
content = df['Text']
News_Tokenizing = News_NLP.tokenize(content)
News_RemoveWords = News_NLP.stopwords_removal()
News_Lemmatizing = News_NLP.lemmatization()
News_POStag = News_NLP.nltk_pos_tag()