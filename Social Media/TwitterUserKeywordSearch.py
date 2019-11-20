import pandas as pd

def keywordsearch():

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
    
    
    # for words in samsunglist:
    #     check = df.Text.str.contains(words, case = False)
    # print(df['Text'].iloc[0])
    count = 0
    usercontent = df['User']
    userdate = df['Date']
    content = df["Tweets"]

    print(len(content))

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

                # df = pd.DataFrame(columns=['Tweets'])
        print(count)
    print(relevantuser)
    print(relevantdate)
    print(relevanttext)

    dfUser = pd.DataFrame(relevantuser, columns = ['User'])
    dfDate = pd.DataFrame(relevantdate, columns = ['Date'])
    dfTweets = pd.DataFrame(relevanttext, columns = ['Tweets'])

    print(dfUser.head(10))

    # print(df['User'].head(10))
    # print(df['Date'].head(10))
    # print(df['Tweets'].head(10))

    # df = pd.DataFrame(relevanttext)


    final = pd.concat([dfUser,dfDate,dfTweets], axis = 1)

    print(final.head())

    # final.sort_values('Tweets', inplace = True)

    # remove duplicate rows

    final.drop_duplicates(subset = 'Tweets' ,keep = 'first', inplace = True)


    pd.DataFrame.from_dict(data = final , orient = 'columns').to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Relevant/' + datafile + 'Relevant.csv')
 
    # df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Relevant/vergeRelevant.csv')
 
 
    #     # print(df['Text'].iloc[0])
            # for i in range(len(df['Text'])):
    
    # for keywords in samsunglist:
    #     if keywords
                
                # if True:

                #     df = df[df.Text.str.contains(words)]

                #     print(words)
                #     print(df)

                #     print(len(df))

                    # df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/Samsung/UserKeywordSearch' + words + '.csv')

                    # i = i + 1

        # if include == True:



        #     print(df)

        #     df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/UserKeywordSearch' + words + '.csv')

        #     print(df.head(10))
        #     i += 1


keywordsearch()
