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
       "galaxy A", "galaxy note", "QLED", "quickdrive", "s series", ]


    i = 0

    for i in range(len(samsunglist)) :
        df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SamsungMobile.csv', names = ['User','ID','Date','Text'])

        search = samsunglist[i]

        df = df[df.Text.str.contains(search)]

        print(df.head(10))

        df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/UserKeywordSearch' + search + '.csv')

        i += 1

        print(i)

keywordsearch()
