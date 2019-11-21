import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

datafile = input('Which user would you like to generate a graph for ?')

df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/' + datafile + '/' + datafile +'SentimentAll.csv')

print(df.head())
