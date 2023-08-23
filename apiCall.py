import requests
import json
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
paramaters = { 'upc' : '073360772023'}
response = requests.get(baseUrl,params=paramaters)
print(response.url)

content = response.content
info = json.loads(content) #json into ictionaries?
item = info['items']
itemInfo = item[0]
title = itemInfo['offers'][0]['title']
brand = itemInfo['brand']
print(title)
print(brand)