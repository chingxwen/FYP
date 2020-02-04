import os
import glob
import pandas as pd
import numpy as np

class concat() :


    def __init__(self):
        pass

    def read_csv(self):
        # directory folder 

<<<<<<< HEAD
        os.chdir(r"C:\Users\User\Desktop\FYP\FYP\Social Media\reddit\MLReady\Comments\Comments")
=======
        # os.chdir(r"C:\Users\User\Desktop\FYP\FYP\Social Media\reddit\MLReady\Comments")
        os.chdir(r"C:\Users\jiajie25\Documents\GitHub\FYP\Social Media\reddit\MLReady\Comments")
>>>>>>> f2145e251f7b5c356f8fb0635f2ea94509db5755

        #include all files in the folder into the list

        extension = 'csv'
        self.all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


    def combine(self):

        #combine all files in the list

        combined_csv = pd.concat([pd.read_csv(f) for f in self.all_filenames ],axis = 0, sort= False)

        df = combined_csv.sort_values(by='timestamp', ascending=True)

        # df.to_csv(r"C:\Users\User\Desktop\FYP\FYP\Social Media\reddit\MLReady\Comments\Concat\All_concat_comments.csv", index=False, encoding='utf-8-sig')
        df.to_csv(r"C:\Users\jiajie25\Documents\GitHub\FYP\Social Media\reddit\MLReady\Comments\Concat\All_concat_comments.csv", index=False, encoding='utf-8-sig')


ComConcat = concat()
ComConcat.read_csv()
ComConcat.combine()