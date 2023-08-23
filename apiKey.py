import requests
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
paramaters = {'APPID':'accountKey', 'q':'Seattle,US'} #APPID - API key form account
response = requests.get(baseUrl, params=paramaters)
print(response.content)