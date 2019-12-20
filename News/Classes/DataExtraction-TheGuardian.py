import pprint
import requests
import pandas as pd
from goose3 import Goose
import os

class DataExtraction:
    "This class handles all the extraction for the news articles from The Guardian"

    
    def __init__(self, api_key, url, query, fromdate, todate, page = 1):
        self.api_key = api_key
        self.url = url
        self.query = query
        self.fromdate = fromdate
        self.todate = todate
        self.page = page


    def NewsExtraction(self):
        # self.api_key = '9c31513f-beb6-4aac-86ee-0b1320f2860b'

        # self.url = 'https://content.guardianapis.com/search?'

        # self.query = "Samsung"#str(input("Query: "))
        # self.fromdate = "2018-07-01"#str(input("From Date (YYYY-MM-DD): "))
        # self.todate = "2019-11-01"#str(input("To Date (YYYY-MM-DD): "))
        # self.page = 1 #int(input("Page Number: "))

        
        df = pd.DataFrame(columns =('Section', 'Title', 'URL', 'Date', 'Text'))
        
        parameters = {
        'q': self.query,
        'from-date': self.fromdate,
        'to-date': self.todate,
        'order-by': 'newest',
        'page-size': 200, #200 max
        'page': self.page,
        'api-key': self.api_key
        }

        print("Current Page Number: " + str(self.page))

        response = requests.get(self.url, params=parameters)
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
extraction = DataExtraction(
    "9c31513f-beb6-4aac-86ee-0b1320f2860b", 
    "https://content.guardianapis.com/search?",
    "Samsung",
    "2018-07-01",
    "2019-11-01")
print(extraction.NewsExtraction())