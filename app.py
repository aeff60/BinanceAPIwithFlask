from asyncio.windows_events import NULL
# from flask import Flask, render_template, make_response, request
from flask import *  
import json
from urllib.request import urlopen
app  = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])  
def home():
    #ที่อยู่ของ API
    url = "https://api.binance.com/api/v1/ticker/price"

    response = urlopen(url)

    data_json = json.loads(response.read())
    
    if request.method == "POST": 
        #  skill = request.form.get('coin')
         selectValuebalance = request.form.get('balance')
         selectValue = request.form.get('coin')
         selectValuecoin = str(selectValue)
    else:
        selectValuecoin = ""
    # data_json is data from api
    return render_template('home.html', data=data_json, result=selectValuecoin, result2=selectValuebalance)  

# @app.route('/home')
# def home2():
    
#     url = "https://api.binance.com/api/v1/ticker/price"

#     response = urlopen(url)

#     data_json = json.loads(response.read())
#     response = urlopen(url)
  

#     data_json = json.loads(response.read())

#     return render_template('home.html', data=data_json)



@app.route('/cookie')  
def cookie():  
    res = make_response("<h1>cookie is set</h1>")  
    res.set_cookie('foo','bar')  
    return res     

# @app.route('/success2',methods = ['POST'])  
# def success():  
#     if request.method == "POST":  
#         cryto = request.form['cryto']  
#         balance = request.form['balance']  
#         resp = make_response(render_template('home.html')) 
#         resp.set_cookie('symbol',cryto)
#         return resp
#     else:
#         return "error"   

@app.route('/h2')  
def login():  
    return render_template("login.html")  


   

@app.route('/success',methods = ['POST'])  
def success():  
    if request.method == "POST":  
        # skill = request.form.get('coin')
        balance = request.form['balance'] 
        # profileList.append(balance)  
        resp = make_response(render_template('home.html',name=balance))
        resp.set_cookie('balance',balance) 
        # balance1 = request.cookies.get('balance')
        # resp = make_response(render_template('home.html',name=balance1))    
        return resp  
    else:  
        return redirect(url_for('error'))  

# @app.route('/success')  
# def profile():     
#   return resp  
    
if __name__ == '__main__':
    app.run(debug=True)    



