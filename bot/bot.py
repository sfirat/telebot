import requests
import pprint

BASE_URL = 'https://api.telegram.org/bot792350544:AAEZE7n3Qai64zlmWshQvmdhrFcHHmznAe4'

r = requests.get(BASE_URL + '/getMe')
r.json()
