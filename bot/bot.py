import requests
import pprint
import misc

BASE_URL = 'https://api.telegram.org/bot'+ BOT_TOKEN

r = requests.get(BASE_URL + '/getMe')
r.json()

