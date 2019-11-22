import numpy as np
import pandas as pd

datafile = input('Which datafile do you want to calculate net ? ')
neg = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/Graphs/Dataset/CSV/SentimentAnalysis/' + datafile + '/' + datafile +'.csv')


print(neg.head(10))

