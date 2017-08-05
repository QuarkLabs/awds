import json, requests

URL = "http://34.209.204.28:5000/sis/calcwater"

def request(cropId, moisture):
    data = {
            'CropId' : cropId,
            'Moisture' : moisture
            }
    resp = requests.post(url=URL, json=data)
    values = json.loads(resp.text)
    return values

## TEST
print(request(1, 25.5))
