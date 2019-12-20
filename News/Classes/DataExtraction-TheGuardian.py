import pprint
import requests
import pandas as pd
from goose3 import Goose
import os


def NewsExtraction():
    api_key = '9c31513f-beb6-4aac-86ee-0b1320f2860b'

    url = 'https://content.guardianapis.com/search?'

    query = "Samsung"#str(input("Query: "))
    fromdate = "2018-07-01"#str(input("From Date (YYYY-MM-DD): "))
    todate = "2019-11-01"#str(input("To Date (YYYY-MM-DD): "))
    page = 1 #int(input("Page Number: "))

    
    df = pd.DataFrame(columns =('Section', 'Title', 'URL', 'Date', 'Text'))
    
    # totalpages = page 
    # while page <= totalpages:

    parameters = {
    'q': query,
    'from-date': fromdate,
    'to-date': todate,
    'order-by': 'newest',
    'page-size': 200, #200 max
    'page': page,
    'api-key': api_key
    }

    print("Current Page Number: " + str(page))

    response = requests.get(url, params=parameters)
    response_json = response.json()['response']['results']
    totalpage = response.json()['response']['pages']
    print(response.json()['response']['total'])
    print("The total number of pages to be extracted: " + str(totalpage))


    g = Goose()

    i = 0
    for article in response_json:
        i = i + 1
        section = article['sectionName']
        title = article['webTitle']
        url = article['webUrl']
        date = article['webPublicationDate']
        text = g.extract(url=url)
        text = text.cleaned_text
        df.loc[i] = section, title, url, date, text
        # page += 1

    export_csv = input("Do you want to export the data to a csv file? Yes or No? ")

    if export_csv.upper() =="YES":
        df.to_csv(parameters["q"] + ".csv", index=False)
        print(os.getcwd())
    else: 
        print(df['Title'])

NewsExtraction()
