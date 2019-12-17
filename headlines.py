import pprint
import requests
secret ='82350f6927f74fca8c3cb5d60e604954'
url = 'https://newsapi.org/v2/top-headlines?'
parameters = {
    'q' : 'news',
    'pageSize' : 10,
    'apiKey' : secret
}
