from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="pub_207422f778de16c8efc49f6c31ab50b1726ad")

# You can pass empty or with request parameters {ex. (country = "us")}

response = api.news_api( q= "ronaldo" , country = "us")
