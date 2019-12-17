import pprint
import requests
secret = '82350f6927f74fca8c3cb5d60e604954'
url = 'https://newsapi.org/v2/top-headlines?country='
parametres = {
    'q': 'news',
    'pagesize' : 20,
    'apikey' : secret
}
response = requests.get(url, params=parametres)
response_json = response.json()
pprint.pprint(response_json)
for i in response_json['articles'] :
    print(i['title'])