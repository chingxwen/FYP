import pprint
import requests
import pandas as pd
from goose3 import Goose

api_key = '9c31513f-beb6-4aac-86ee-0b1320f2860b'

url = 'https://content.guardianapis.com/search?'

query = str(input("Query: "))
fromdate = input("From Date: ")
page = str(input("Page Number: "))

# if len(query) == 0:
#     query = "samsung"
#     print(query)
parameters = {
    'q': query,
    'from-date': fromdate
    'order-by': 'newest',
    'page-size': 200, #200 max
    'page': page,
    'api-key': api_key
}

response = requests.get(url, params=parameters)

# article_count = response.json()['totalResults']
response_json = response.json()['response']['results']

g = Goose()

df = pd.DataFrame(columns =('Section', 'Title', 'URL', 'Date', 'Text'))
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
# print("Total Articles: " + str(article_count))

export_csv = input("Do you want to export the data to a csv file? Yes or No? ")

if export_csv.upper() =="YES":
    df.to_csv("TheGuardianData.csv", index=False)
else: 
    print(df['Title'])
