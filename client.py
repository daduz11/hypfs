import requests
PARAMS = {'nm': 'ciao mondo'}
r = requests.get(url='http://127.0.0.1:5000', params=PARAMS)
print(r.text)