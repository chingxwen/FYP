from Classes import TwitterConcat
from Classes import UserCleanse
from Classes import UserKeywordSearch
from Classes import TwitterSentiment

path = input("Please input the filepath for the files to be downloaded to: ")

Concat = TwitterConcat.concat(path)
Concat.read_csv()
Concat.combine()

TwitterCleanse = UserCleanse.UserClense(path)
TwitterCleanse.read_Csv()
TwitterCleanse.drop_columns()
TwitterCleanse.cleanse_data()
TwitterCleanse.export()

TwitterCleanse = UserKeywordSearch.UserKeywordSearch(path)
TwitterCleanse.read_file()
TwitterCleanse.searchloop()
TwitterCleanse.export()

TwitterSenti = TwitterSentiment.VaderSentiment(path)
TwitterSenti.read_csv()
TwitterSenti.extract_column()
TwitterSenti.sentimentanalysis()



