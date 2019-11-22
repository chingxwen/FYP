import pandas as pd
import re
import dateutil.parser as dparser
from dateutil.tz import tzutc
import datefinder
from datetime import datetime

datafile = input('Which DataSet do you want to Format ? ')
df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/' + datafile + '.csv')

# print(type(df))

dflist = df.values.tolist()
date = []
for i in range (len(dflist)):
    match = re.search(r'\d{4}-\d{2}-\d{2}',str(dflist[i]))
    date.append(datetime.strptime(match.group(), '%Y-%m-%d').date())
print(date)
# date = []
# for i in range (len(dflist)):
#     date.append(dparser.parse(str(dflist[i]),fuzzy = True))
# print(date)

dfdate = pd.DataFrame(date)
print(dfdate)

final = pd.concat([df,dfdate],axis=1)
print(final)

final.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Keywords/Format/New' + datafile + '.csv')
print('Written')