import pandas as pd


def keywordsearch():

    df = pd.read_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/SamsungMobile.csv', names = ['User','ID','Date','Text'])

    search = input('What keywords would you like to search for ? ')\

    df = df[df.Text.str.contains(search)]

    df.to_csv('C:/Users/User/Desktop/FYP/FYP/Social Media/CSV/UserKeywordSearch.csv')

    print(df.head(10))

keywordsearch()

