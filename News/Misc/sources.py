import pandas as pd
from newsapi import NewsApiClient
import newsapi

newsapi = NewsApiClient( api_key='daaea43db9ff4faf84cb6924276093d3')
sources = newsapi.get_sources()['sources']

i = 0
df = pd.DataFrame(columns =("Name", "ID", "URL"))
for source in sources:
    i = i + 1
    name = source['name']
    source_id = source['id']
    url = source['url']
    df.loc[i] = name, source_id, url

df.to_csv("sources.csv", index = False)







# pd.DataFrame.from_dict(data=sources, orient='columns').to_csv('NewsApiDataSources.csv', header=True)
