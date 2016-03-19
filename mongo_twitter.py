__author__ = 'dhana013'

from tweepy import API
lookup ='BigData'
api = API()

search = []
page = 1
maxPage = 10
while(page<=maxPage):
    tweets = api.search(lookup,page = page)
    for tweet in tweets:
        search.append(tweet)
    page = page + 1