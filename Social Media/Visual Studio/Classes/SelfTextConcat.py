import os
import glob
import pandas as pd
import numpy as np

class concat() :


    def __init__(self,path):
        self.path = path
        pass

    def read_csv(self):

        # directory folder 
        os.chdir(input('Filepath for files to concat SelfText? '))

        #include all files in the folder into the list
        extension = 'csv'
        self.all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


    def combine(self):

        #combine all files in the list
        combined_csv = pd.concat([pd.read_csv(f) for f in self.all_filenames ],sort=False)

        df = combined_csv.sort_values(by='timestamp', ascending=True)

        df.to_csv(self.path + "\\SelfText" + "\\Concat" + "\\All_concat_selftext.csv", index=False, encoding='utf-8-sig')


# SelfConcat = concat()
# SelfConcat.read_csv()
# SelfConcat.combine()
