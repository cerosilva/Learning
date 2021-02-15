import requests
import json

response = requests.get('http://sevenninethree.org')
print(response)
print(response.status_code)

if response:
    print('request is successful')
else:
    print('Request returned an error')

spotifyresponse = requests.get("http://api.open-notify.org/astros.json")

print(spotifyresponse)
print(spotifyresponse.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(spotifyresponse.json())


parameters = {
    "lat": 15.18,
    "lon": 73.57   
}


isspassresponse = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print(isspassresponse)
print(isspassresponse.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(isspassresponse.json())

pass_times = isspassresponse.json()['response']

jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)    
