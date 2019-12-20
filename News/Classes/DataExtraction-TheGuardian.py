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
    
    def RetrieveData(self, parameters):
        
        print("Current Page Number: " + str(self.page))

        response = requests.get(self.url, params=parameters)
        totalpage = response.json()['response']['pages']
        # response_json = response.json()['response']['results']
        print("The total number of articles to be printed " + str(response.json()['response']['total']))
        print("The total number of pages to be extracted: " + str(totalpage))
        return (response, self.page, totalpage)


    def AddPages(self):
        self.page += 1
        return self.page


    def NewsExtraction(self, response):
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
        
        export_csv = input("Do you want to export the data to a csv file? Yes or No? ")
        if export_csv.upper() =="YES":
            df.to_csv(config["q"] +"_" + str(self.page) + ".csv", index=False)
        else: 
            print(df['Title'])
            print(df.shape)




extraction = DataExtraction(
    "9c31513f-beb6-4aac-86ee-0b1320f2860b", 
    "https://content.guardianapis.com/search?",
    input("Which Company? "),
    "2018-07-01",
    "2019-11-01",)

config = extraction.NewsConfig()
data = extraction.RetrieveData(config) 
extraction.NewsExtraction(data[0])

while data[1] <= data[2]:
    print(str(data[1]) + "/" + str(data[2]))
    extraction.AddPages()
    config = extraction.NewsConfig()
    data = extraction.RetrieveData(config) 
    extraction.NewsExtraction(data[0])

concat_csv = input("Do you want to concatenate the csv files into a single csv file? Yes or No? ")
if concat_csv.upper() =="YES":
    files = []
    li = []
    for i in range(1,(data[2] + 1)):
        files.append(config["q"] +"_" + str(i) + ".csv")

    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    combined = pd.concat(li, axis=0, ignore_index=True)
    combined.to_csv(config["q"] + ".csv", index=False)

    for filename in files:
        os.remove(filename)
