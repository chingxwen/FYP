import os
import glob
import pandas as pd
import numpy as np

class concat() :


    def __init__(self, path):

        self.path = path

    def read_csv(self):

        # directory folder 
        os.chdir(input('Please input the folder path for concatenation'))

        #include all files in the folder into the list
        extension = 'csv'
        self.all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    
      
    def combine(self):
        columns = ['User','ID','Date','Tweets']
        
        #combine all files in the list
        combined_csv = pd.concat([pd.read_csv(f, names = columns) for f in self.all_filenames ],sort = True, axis = 0)
    
        df = combined_csv.sort_values(by='Date', ascending=True)

        df.to_csv(self.path + "\\Concat" + "\\TwitterConcat.csv", index=False, encoding='utf-8-sig')


# Concat = concat()
# Concat.read_csv()
# Concat.combine()
