from flask import Flask
from flask import Flask, render_template
from binance.client import Client
import json
from pprint import pprint

app  = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about')
def about():
    
    api_key = 'VN4aWcnxQzBqRhcMJ7SwKWavIs1goZDcLQ8oSx9s2WnA7ztpYgqosJkymEc1xogF'
    api_secret = 'fNYc0CWm9CYPhBo7rTcX5RfV7MNsMIivcrdYHYycdQCFmrQ0U67vwgKHnuW2zcNO'

    client = Client(api_key, api_secret)

    info = client.get_account()
    # pprint(info)

    # doge = client.get_asset_balance(asset='DOGE')
    # usdt = client.get_asset_balance(asset='USDT')

    # print('DOGE:', doge)
    # print('USDT:', usdt)
    
    print(info['balances'])
    
    tempHTML = ""
    
    for asset in info['balances']:
        
        tempHTML.join("<li>",asset,"</li>")
        
        print(asset['asset'])

    return tempHTML

if __name__ == '__main__':
    app.run(debug=True)    
