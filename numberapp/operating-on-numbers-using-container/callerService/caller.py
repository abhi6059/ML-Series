from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route("/",methods=['POST'])
def caller():
    payload = request.get_json()

    sqrurl = 'http://sqrapp:5020/'
    sqrres = requests.post(sqrurl,json=payload)
    sqrdata = sqrres.json()
    sqrnum1 = int(sqrdata['num1'])
    sqrnum2 = int(sqrdata['num2'])

    cubeurl = 'http://cubeapp:5030/'
    cuberes = requests.post(cubeurl,json=payload)
    cubedata = cuberes.json()
    cubenum1 = int(cubedata['num1'])
    cubenum2 = int(cubedata['num2'])

    finalpayload = {
        "num1" : sqrnum1,
        "num2" : sqrnum2,
        "num3" : cubenum1,
        "num4" : cubenum2
    }

    addurl = 'http://addapp:5040/'
    addres = requests.post(addurl,json=finalpayload)
    add_data = addres.json()
    addresult = add_data['result']

    return jsonify(sqrnum1=sqrnum1,
    sqrnum2=sqrnum2, cubenum1=cubenum1, 
    cubenum2=cubenum2, theresult=addresult)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5010,debug=True)


