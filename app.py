from flask import Flask
from flask import Flask, render_template

app  = Flask(__name__)

@app.route('/')

def home():
    api_key = 'VN4aWcnxQzBqRhcMJ7SwKWavIs1goZDcLQ8oSx9s2WnA7ztpYgqosJkymEc1xogF'
    api_secret = 'fNYc0CWm9CYPhBo7rTcX5RfV7MNsMIivcrdYHYycdQCFmrQ0U67vwgKHnuW2zcNO'

    client = Client(api_key, api_secret)

    info = client.get_account()


    for asset in info['balances']:
        data = asset['asset']
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)    
