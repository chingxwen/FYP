
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

data = pd.read_csv("C:/Users/olivi/Documents/fyp/samsungtech15-19.csv")
print(data)

import numpy as np


data['High'] = data['High'].replace('null', np.nan)
df = data.dropna(axis=0, subset=['High'])



#pd.DataFrame.from_dict(data=df, orient='columns').to_csv("C:/Users/olivi/Documents/fyp/cleaned3samsungtech1519.csv")
df.rename(columns={'Adj Close':'adj_close', 'Date':'date'}, inplace = True)

print(df)

print(type(df.loc[df('date')]))


