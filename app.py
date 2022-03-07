from asyncio.windows_events import NULL
from flask import *  
import json
from urllib.request import urlopen
app  = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def home():
    global selectValuecoinstr, selectValuebalancestr
    #ที่อยู่ของ API
    url = "https://api.binance.com/api/v1/ticker/price"

    response = urlopen(url)

    data_json = json.loads(response.read()) #ข้อมูลที่เป็น dictionary จาก api
    
    if request.method == "POST": 
        
         selectValuecoin = request.form.get('coin') #ข้อมูลชื่อเหรียญจาก dropdown
         selectValuecoinstr = str(selectValuecoin) #ข้อมูลชื่อเหรียญจาก dropdown แปลงเป็น string
         selectValuebalance = request.form.get('balance') #ข้อมูลจากจำนวนเหรียญที่มีตอนกรอก
         selectValuebalancestr = str(selectValuebalance)#ข้อมูลจากจำนวนเหรียญที่มีตอนกรอก แปลงเป็น string
        #  return render_template('home.html', data=data_json, coinsymbol=selectValuecoinstr, valuebalance=selectValuebalancestr)
         
    else:
        
        selectValuecoinstr = " "
        selectValuebalancestr = " "
    return render_template('home.html', data=data_json, coinsymbol=selectValuecoinstr, valuebalance=selectValuebalancestr)  
    
if __name__ == '__main__':
    app.run(debug=True)    



