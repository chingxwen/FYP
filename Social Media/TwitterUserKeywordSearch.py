import pandas as pd

def keywordsearch():

    samsunglist =["samsung","galaxy", "samsung galaxy", "samsung group", 
        "samsung technologies","galaxy s10", "galaxy note10", "galaxy fold", 
        "galaxy s10+", "galaxy s10e", "galaxy buds", "galaxy watch", "watch active 2",
        "galaxy tab", "tab S6", "galaxy book S", "samsung electronics", "samsung x IFA 2019", 
        "the wall luxury", "Q series soundbar", "seoul sisters conference", 
        " Samsung Semiconductor Institute of Technology", "galaxy A30", "galaxy S11", 
        "a70 waterproof", "a70 wireless charging", "s10 plus", "s7 edge", "galaxy m30", "galaxy j7", 
       "galaxy j2", "galaxy a10", "space zoom", "samsung support", "the serif", "#dowhatyoucant", "spacemax", 
       "galaxy A", "galaxy note", "QLED", "quickdrive", "s series"]


    df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SamsungMobile.csv', names = ['User','Date','Text'])
    
    
    # for words in samsunglist:
    #     check = df.Text.str.contains(words, case = False)
    # print(df['Text'].iloc[0])
    count = 0
    content = df["Text"]
    for words in samsunglist:
        for i in range(len(content)):
            if (words in content.iloc[i]) == True:
                print(words)
                count += 1 
                print(content.iloc[i])

                # df = pd.DataFrame(columns=['Tweets'])
    print(count)

        # print(df['Text'].iloc[0])
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
