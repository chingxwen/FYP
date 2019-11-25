import os
import glob
import pandas as pd
import numpy as np

os.chdir(r"C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/Net File")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])


# Removal of Null Values
combined_csv.replace('',np.nan,inplace=True)
combined_csv.dropna(axis = 0, how = 'any', inplace = True)
print(combined_csv.head(10))
combined_csv.index = pd.MultiIndex.from_arrays([combined_csv.index])

#export to csv
combined_csv.to_csv("All_source_Name.csv", index=False, encoding='utf-8-sig')