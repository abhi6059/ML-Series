from flask import Flask,request,jsonify
import math
app = Flask(__name__)
@app.route("/",methods=['POST'])
def add():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    num3 = int(data['num3'])
    num4 = int(data['num4'])
    res = num1+num2+num3+num4
    return jsonify(result=res)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5040,debug=True)
