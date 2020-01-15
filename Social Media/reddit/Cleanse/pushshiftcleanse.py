import pandas as pd 
import csv
import re

df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/pushshiftandroid.csv')

#remove duplicate rows
df.drop_duplicates(subset = 'title' ,keep = 'first', inplace = True)

df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/reddit/Data/Cleanse/pushshiftandroidcleanse.csv')