from Class import TwitterConcat
from Class import UserCleanse
from Class import UserKeywordSearch
from Class import TwitterSentiment

path = input("Please input the filepath for the files to be downloaded to: ")

#Twitter concat
Concat = TwitterConcat.concat(path)
Concat.read_csv()
Concat.combine()

#twitter cleanse
TwitterCleanse = UserCleanse.UserClense(path)
TwitterCleanse.read_Csv()
TwitterCleanse.drop_columns()
TwitterCleanse.cleanse_data()
TwitterCleanse.export()

#twitter keyword search
TwitterCleanse = UserKeywordSearch.UserKeywordSearch(path)
TwitterCleanse.read_file()
TwitterCleanse.searchloop()
TwitterCleanse.export()

#twitter sentiment
TwitterSenti = TwitterSentiment.VaderSentiment(path)
TwitterSenti.read_csv()
TwitterSenti.extract_column()
TwitterSenti.sentimentanalysis()



