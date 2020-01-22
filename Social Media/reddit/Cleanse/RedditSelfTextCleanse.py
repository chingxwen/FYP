import pandas as pd 
import csv
import re
import datetime as dt
import numpy as np

datafile = input('whcih file would you like to clense?')
df = pd.read_csv('C:/FYP/Social Media/reddit/Data/Pulled/raw/' + datafile + '.csv', )

df.sort_values("id", inplace = True)
df.drop_duplicates(subset="id", keep="first", inplace=True)
print(df)
#Converting datetime column from UNIX to normal
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = df["created"].apply(get_date)
df = df.assign(timestamp = _timestamp)

print(df)

