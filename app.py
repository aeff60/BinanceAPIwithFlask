import os
from flask import *  
import json
from urllib.request import urlopen

from numpy import double, float64
app  = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def home():
    global selectValuecoinstr, selectValuebalancestr
    data_jsonsymbol = ""
    #ที่อยู่ของ API
    url = "https://api.binance.com/api/v1/ticker/price"

    response = urlopen(url)

    data_json = json.loads(response.read())
    data_list = []
    for i in range(len(data_json)):
        dataprice= data_json[i]['symbol']
        a = dataprice.find("USDT")
        if a != -1:
            data_list.append(data_json[i])
        else:
            pass


    data_list2 = []
    data_list3 = []
    for j in range(len(data_list)):
        datasymbol2 = data_list[j]['symbol']
        dataprice2 = data_list[j]['price']
        data_list2.append(datasymbol2)
        data_list3.append(dataprice2)
        # dataprice2 = data_list[j]['price']

    listCookie = []
    if request.method == "POST": 
         selectValuecoin = request.form.get('coin') 
         selectValuecoinstr = str(selectValuecoin) 
         print(selectValuecoinstr)
     

         selectValuebalance = request.form.get('balance') 
         selectValuebalancestr = str(selectValuebalance)
         print(selectValuebalancestr)
        
        
         for o in range(len(data_list2)):
            datasymbol3 = data_list2[o]
            datasymbol4p = data_list3[o]
            a2 = datasymbol3.find(selectValuecoinstr)
            if a2 != -1:
                price = datasymbol4p
                
            else:
                pass

         listCookie = json.loads(request.cookies.get('symbol'))

         data_jsonsymbol = double(selectValuebalancestr) * double(price)
         listCookie.append([selectValuecoinstr, selectValuebalancestr, data_jsonsymbol])
         #listCookie = str(listCookie)
                
    else:
        selectValuecoinstr = " "
        selectValuebalancestr = "0"
    print(listCookie)
    resp = make_response(render_template('home.html', mycoin=listCookie, data=data_list2, coinsymbol=selectValuecoinstr, valuebalance=selectValuebalancestr, data_jsonsymbol=data_jsonsymbol))
    resp.set_cookie('symbol',json.dumps(listCookie)) 
    return resp
      
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
   



