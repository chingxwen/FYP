import pandas as pd
import numpy as np
import re
import nltk
from pprint import pprint
from textblob import TextBlob
import csv

class senti_value:
   def __inti__(self):
      pass

   #Join tokenised words for each article
   def joinContent(self, content):
      self.joinedText = []
      for articles in content:
         self.joinedText.append(" ".join(articles))
      print("Text has been joined")
      return self.joinedText

   #Get sentiment value for each article
   def sentiScore(self):
      self.sentiment = []
      for articles in self.joinedText:
         blob = TextBlob(articles)
         self.sentiment.append(blob.sentiment.polarity)
      print(self.sentiment)
      print("Retrieved sentiment score")
      return self.sentiment

   #Export cleansed content to a csv file
   def exportCSV(self, filepath):
      self.sentiment1 = pd.DataFrame(self.sentiment)
      # self.sentiment = pd.Series(self.sentiment)
      self.sentiment1.to_csv(filepath, index = False)