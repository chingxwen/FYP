import pandas as pd

def keyword_search():

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

    datafile = input('Which data set do you want to cleanse?')
    df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Cleanse/' + datafile + 'Cleanse.csv', names = ['User','Date','Tweets'])
    
    count = 0
    usercontent = df['User']
    userdate = df['Date']
    content = df["Tweets"]

    print(len(content))

    #for loop to run through every row in datafile
    #inside the for loop is a if else loop to check for relvent data rows using the samsung dictionary
    #Append relevent rows into a new list then convert into a dataframe 

    relevantuser = []
    relevantdate = []
    relevanttext = []
    for words in samsunglist:
        for i in range(len(content)):
            if (words in content.iloc[i].lower()) == True:
                print(words)
                count += 1 
                print(content.iloc[i])

                relevantuser.append(usercontent.iloc[i])
                relevantdate.append(userdate.iloc[i])
                relevanttext.append(content.iloc[i])

    print(relevantuser)
    print(relevantdate)
    print(relevanttext)

    dfUser = pd.DataFrame(relevantuser, columns = ['User'])
    dfDate = pd.DataFrame(relevantdate, columns = ['Date'])
    dfTweets = pd.DataFrame(relevanttext, columns = ['Tweets'])


    final = pd.concat([dfUser,dfDate,dfTweets], axis = 1)

    # remove duplicate rows
    final.drop_duplicates(subset = 'Tweets' ,keep = 'first', inplace = True)

    # Convert DataFrame to csv
    pd.DataFrame.from_dict(data = final , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Relevant/' + datafile + 'Relevant.csv')

    

keyword_search()
