from urllib.request import urlopen
  

import json

url = "https://api.binance.com/api/v1/ticker/price"
  

response = urlopen(url)
  

data_json = json.loads(response.read())
symbolList = [] 
for i in range(len(data_json)):
    v = data_json[i].get('symbol')
    symbolList.append(v)
    # print(type(v))
    
print(data_json)




