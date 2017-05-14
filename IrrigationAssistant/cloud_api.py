from flask import Flask, url_for, request, json, Response
from main import *

app = Flask(__name__)

@app.route('/sis/calcwater', methods = ['POST'])
def getvalues():
    data = json.loads(json.dumps(request.json)) 
    print("\n==========")
    print("Receiving..", data)

    print("Processing..")
    values = calcValues(data)
    js = json.dumps(values)
    resp = Response(js, status =200, mimetype = 'application/json')
    
    print("Sending..", values)
    return resp

def calcValues(data):
    print("aaa")
    waterAmount = get_water(data['CropId'], data['Moisture'])
    values = {
            "CropId" : data['CropId'],
            "WaterAmount" : waterAmount
            }
    return values

if __name__ == '__main__':
    print("Listening...")
    app.run(host='0.0.0.0', port=5000)
