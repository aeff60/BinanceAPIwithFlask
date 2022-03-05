from asyncio.windows_events import NULL
from flask import Flask
from flask import Flask, render_template
import json
from urllib.request import urlopen

app  = Flask(__name__)

@app.route('/')

def home():
    
    url = "https://api.binance.com/api/v1/ticker/price"

    response = urlopen(url)

    data_json = json.loads(response.read())
    response = urlopen(url)
  

    data_json = json.loads(response.read())
    symbolList = []
    a = 1
    for i in range(len(data_json)):
        symbol = data_json[i].get('symbol')
        symbolList.append(symbol)
    return render_template('home.html', data=data_json)

@app.route('/about')
def about():
    url = "https://api.binance.com/api/v1/ticker/price"
    response = urlopen(url)
    data_json = json.loads(response.read())
    response = urlopen(url)
    data_json = json.loads(response.read())
    symbolList = []
    for i in range(len(data_json)):
        symbol = data_json[i].get('symbol')
        symbolList.append(symbol)
    return data_json
    
if __name__ == '__main__':
    app.run(debug=True)    
