from flask import Flask,request,jsonify
import math
app = Flask(__name__)
@app.route("/",methods=['POST'])
def cube():
    data = request.get_json()
    num1 = int(data['num1'])
    num2 = int(data['num2'])
    num1 = math.pow(num1,3)
    num2 = math.pow(num2,3)
    return jsonify(num1 = num1,
    num2 = num2)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5030,debug=True)
