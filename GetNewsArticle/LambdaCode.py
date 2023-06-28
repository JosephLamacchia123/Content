import unicodedata
import requests
from newspaper import Article
import json

def getNewsArticle():
    site = "https://gnews.io/api/v4/top-headlines?lang=en&country=us"
    params = {
        "category": "nation",
        "max": "1",
        "apikey": "20b9104ce03229cff48aa78a604b2f0c",
    }

    response = requests.request("GET", site, params=params)

    #function test by printing article titles, can be removed
    title = response.json().get("articles")[0].get("title")

    url = response.json().get("articles")[0].get("url")

    article_site = Article(url)
    article_site.download()
    article_site.parse()

    article = { "title": title.encode("ascii", "ignore").decode('utf-8'), "text": article_site.text.encode("ascii", "ignore").decode('utf-8').replace('\n','') }
    print(json.dumps(article))
    return(json.dumps(article))

getNewsArticle()

"""
Bing Version

def getNewsArticle():
    site = "https://api.bing.microsoft.com/v7.0/news/trendingtopics"
    count = 2
    headers = {
        "Ocp-Apim-Subscription-Key": "a97cb4f904c344098c959f46964d844b"
    }

    response = requests.request("GET", site, headers=headers)

    #function test by printing article titles, can be removed
    titles = [] 
    for x in range(count):
        titles.append(response.json().get("value")[x].get("query"))
        print(titles[x])

    return response.json()['value']

getNewsArticle()
"""