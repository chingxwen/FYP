import pandas as pd
import matplotlib.pyplot as plt


#read train data 
df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/ChannelNewsAsiaCleanse.csv')

ax = df['Tweets'].value_counts(sort=False).plot(kind='barh')
ax.set_xlabel("Number of Samples in training Set")
ax.set_ylabel("Label")
