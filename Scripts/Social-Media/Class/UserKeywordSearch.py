import pandas as pd

class UserKeywordSearch:

    def __init__(self, path):
         
        self.path = path

    def read_file(self):
        
        #read csv
        self.df = pd.read_csv(self.path + "\\Cleanse" + "\\TwitterCleanse.csv", names = ['User','Date','Tweets'])
    
        return self.df

        #for loop to run through every row in datafile
        #inside the for loop is a if else loop to check for relvent data rows using the samsung dictionary
        #Append relevent rows into a new list then convert into a dataframe 

    def searchloop(self):

        relevantuser = []
        relevantdate = []
        relevanttext = []
        content = self.df['Tweets']
        usercontent = self.df['User']
        userdate = self.df['Date']
        content = content.astype(str)

        #Samsung Dictionary
        samsunglist = ["samsung","galaxy", "samsung galaxy", "samsung group", 
            "samsung technologies","galaxy s10", "galaxy note10", "galaxy fold", 
            "galaxy s10+", "galaxy s10e", "galaxy buds", "galaxy watch", "watch active 2",
            "galaxy tab", "tab S6", "galaxy book S", "samsung electronics", "samsung x IFA 2019", 
            "the wall luxury", "Q series soundbar", "seoul sisters conference", 
            " Samsung Semiconductor Institute of Technology", "galaxy A30", "galaxy S11", 
            "a70 waterproof", "a70 wireless charging", "s10 plus", "s7 edge", "galaxy m30", "galaxy j7", 
            "galaxy j2", "galaxy a10", "space zoom", "samsung support", "the serif", "#dowhatyoucant", "spacemax", 
            "galaxy A", "galaxy note", "QLED", "quickdrive", "s series", "galaxyAs", "samsung mobile", "SamsungMobileSA",
            "#DontFumbleTheBag", "galaxy a30s", "#FillUpRoyalBafokeng", "#SDC19", "galaxy buds", "samsungUS", "samsungsupport",
            "chromebook", "samsung J4", "samsung J4 core", "galaxy J4", "galaxy J2", "galaxy J4 core", "galaxy tab",
            "samsung health", "SamsungKids", "SamsungKidsUS", "samsung galacy", "TeamGalaxy", "#TeamGalaxy", "withgalaxy",
            "galaxy FIT E", "samsung T5", "galaxy T5", "Samsung Catalyst Fund", "samsungcatalyst", "SamsungCEOSummit",
            "Samsung 5G Exynos 980", "SamMobile"]

        #loop to search for words in samsung dictionary 

        for words in samsunglist:
            for i in range(len(content)):
                print(content.iloc[i])
                if (words in content.iloc[i].lower()) == True:
                    print(words)
                    global count
                    print(content.iloc[i])

                    relevantuser.append(usercontent.iloc[i])
                    relevantdate.append(userdate.iloc[i])
                    relevanttext.append(content.iloc[i])

        print(relevantuser)
        print(relevantdate)
        print(relevanttext)

        #convert list to dataframe
        dfUser = pd.DataFrame(relevantuser, columns = ['User'])
        dfDate = pd.DataFrame(relevantdate, columns = ['Date'])
        dfTweets = pd.DataFrame(relevanttext, columns = ['Tweets'])

        #convert list to dataframe and concat together
        self.final = pd.concat([dfUser,dfDate,dfTweets], axis = 1)

        return self.final

    def concat(self):

        # remove duplicate rows
        self.final.drop_duplicates(subset = 'Tweets' ,keep = 'first', inplace = True)

    def export(self):

        # Convert DataFrame to csv
        df = pd.DataFrame.from_dict(data = self.final , orient = 'columns').to_csv(self.path + "\\KeywordSearch" + "\\TwitterKeyword.csv")

        return df
        

# TwitterCleanse = UserKeywordSearch()
# TwitterCleanse.read_file()
# TwitterCleanse.searchloop()
# TwitterCleanse.export()

