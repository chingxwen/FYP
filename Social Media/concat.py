import os
import glob
import pandas as pd
import numpy as np

# directory folder 
os.chdir(r"C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SentimentAnalysis/Net File")

#include all files in the folder into the list
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv("All_source_Name.csv", index=False, encoding='utf-8-sig')