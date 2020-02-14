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

    #Define parameters
    def NewsConfig(self):

        parameters = {
        'q': self.query,
        'from-date': self.fromdate,
        'to-date': self.todate,
        'order-by': 'newest',
        'page-size': 200,
        'page': self.page,
        'api-key': self.api_key
        }
        return parameters
    
    #Extract data
    def RetrieveData(self, parameters):
        
        print("Current Page Number: " + str(self.page))

        response = requests.get(self.url, params=parameters)
        totalpage = response.json()['response']['pages']
        print("The total number of articles to be printed " + str(response.json()['response']['total']))
        print("The total number of pages to be extracted: " + str(totalpage))
        return (response, self.page, totalpage)

    #Add page count
    def AddPages(self):
        self.page += 1
        return self.page

    #Extract news content
    def NewsExtraction(self, response, config, filepath):
        df = pd.DataFrame(columns =('Section', 'Title', 'URL', 'Date', 'Text'))
        response_json = response.json()['response']['results']
        g = Goose()

        i = 0
        for article in response_json:
            i = i + 1
            print
            section = article['sectionName']
            title = article['webTitle']
            url = article['webUrl']
            date = article['webPublicationDate']
            text = g.extract(url=url)
            text = text.cleaned_text
            df.loc[i] = section, title, url, date, text
            df.to_csv(filepath + "\\" + config["q"] + "_" + str(self.page) + ".csv", index=False) 
            print(df['Title'])