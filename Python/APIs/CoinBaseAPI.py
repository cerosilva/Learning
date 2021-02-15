import requests
import json
import datetime

cbresponse = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

print(cbresponse.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(cbresponse.json())    


bpis = []

for d in cbresponse:
    bpi = d[bpis]
    bpis.append(bpi)

print(bpi)  