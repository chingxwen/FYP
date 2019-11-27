import pandas as pd
import re
import dateutil.parser as dparser
from dateutil.tz import tzutc
import datefinder
from datetime import datetime

# read csv
datafile = input('Which DataSet do you want to Format ? ')
df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/' + datafile + '.csv')


# converting dataframe to list
dflist = df.values.tolist()

# loop to search for date in string , extract and remove date from string 
# append into array called date
date = []
for i in range (len(dflist)):
    match = re.search(r'\d{4}-\d{2}-\d{2}',str(dflist[i]))
    date.append(datetime.strptime(match.group(), '%Y-%m-%d').date())
print(date)

#convert array date into Data frame 
dfdate = pd.DataFrame(date)
print(dfdate)

#concat the different columns together
final = pd.concat([df,dfdate],axis=1)
print(final)

#output into a csv file
final.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/Format/New' + datafile + '.csv')
print('Written')