import pprint
import requests
import pandas as pd
import sys

api_key = 'daaea43db9ff4faf84cb6924276093d3'

url = 'https://newsapi.org/v2/everything?'

# query = str(input("Please input the news to be searched: "))
query = 'Samsung'
source_input = str(input("Which source to pull the news from? "))


parameters = {
    'q': query, # query phrase
    'pageSize': 100,  # maximum is 100
    'apiKey': api_key, 
    'sources': source_input
}

response = requests.get(url, params=parameters)

article_count = response.json()['totalResults']
response_json = response.json()['articles']

df = pd.DataFrame(columns =('Source', 'Author', 'Title', 'Description', 'Content', 'URL', 'Published Data'))
i = 0
for article in response_json:
    i = i + 1
    source = article['source']['name']
    author = article['author']
    if type(author) != str:
        author = ""
    title = article['title']
    description = article['description']
    content = article['content']
    url = article['url']
    date = article['publishedAt']
    df.loc[i] = source, author, title, description, content, url, date
print("Total Articles: " + str(article_count))

export_csv = input("Do you want to export the data to a csv file? Yes or No? ")

if export_csv.upper() =="YES":
    path = r"D:\Final Year Project\News Data Pulled\Samsung\\" + source_input + ".csv"
    df.to_csv(path, index=False)
    print(path)
else: 
    print(df)

