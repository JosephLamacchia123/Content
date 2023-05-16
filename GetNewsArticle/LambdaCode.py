import requests

def getNewsArticle():
    site = "https://gnews.io/api/v4/top-headlines?lang=en&country=us"
    count = 2
    params = {
        "category": "nation",
        "max": str(count),
        "apikey": "20b9104ce03229cff48aa78a604b2f0c",
    }

    response = requests.request("GET", site, params=params)

    #function test by printing article titles, can be removed
    titles = [] 
    for x in range(count):
        titles.append(response.json().get("articles")[x].get("title"))
        print(titles[x])

    return response.json()['articles']

getNewsArticle()