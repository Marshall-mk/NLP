# collecting data from JSON

import requests
import json

url = 'https://quotes.rest/qod.json'
r = requests.get(url)
res = r.json()
print(json.dumps(res,indent = 4))

q = res['contents']['quotes'][0]
#print only qoutes
print(q['quotes'], '\n--',q['author'])