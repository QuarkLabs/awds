from flask import Flask, url_for, request, json, Response
from main import *

app = Flask(__name__)

@app.route('/sis/calcwater', methods = ['GET', 'POST'])
def getvalues():
    #~ data = json.loads(json.dumps(request.json)) 
    print("\n=========================================================================")
    #~ print("Receiving..", data)
    print(request.args)

    data = {
            "CropId" : str(request.args.get("CropId")),
            "Moisture" : str(request.args.get("Moisture")),
            "Temperature" : str(request.args.get("Temperature"))
            }

    print("Processing..")
    values = calcValues(data)
    js = json.dumps(values)
    resp = Response(js, status =200, mimetype = 'application/json')

    print "DONE!"    
    return resp

#~ @app.route('/sis/calcwater', methods = ['GET'])
#~ def getValuesGet():
    #~ data = json.loads(json.dumps(request.json))
    #~ print("\n==========")
    #~ print("Receiving..", data)

    #~ print("Processing..")
    #~ values = calcValues(data)
    #~ resp = Response(values, status =200, mimetype = 'application/json')

    #~ print("Sending..", values)
    #~ return resp


def calcValues(data):
    print("Calculating water amount.....")
    waterAmount = get_water(data['CropId'], data['Moisture'], data['Temperature'])
    waterAmount = abs(round(waterAmount, 3))
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    print "WATER AMOUNT FOR CROP", data['CropId'], ":[ ", waterAmount, "]"
    print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    values = {
            "CropId" : data['CropId'],
            "WaterAmount" : waterAmount
            }
    return values

if __name__ == '__main__':
    #~ print(calcValues({"CropId":"2"}))
    print("Listening...")
    app.run(host='0.0.0.0', port=5000)
