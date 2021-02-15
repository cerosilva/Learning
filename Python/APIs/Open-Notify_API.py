import requests
import json
import datetime

# Making the API request

spotifyresponse = requests.get("http://api.open-notify.org/astros.json")

print(spotifyresponse)
print(spotifyresponse.json())

# converting the JSON dump into a preformatted string 

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(spotifyresponse.json())

# using the API with query parameters 

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

# Using loop to extract 5 risetimes from above

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)    

# used the Python datetime.fromtimestamp() method to convert the rise times into easier to understand times

from datetime import datetime

times = []

for rt in risetimes:
    time = str(datetime.fromtimestamp(rt))    # Just for fun as i had got an error on line 66, converted to string
    times.append(time)

print(times)
print(time) 
print("The ISS will pass over Margao at "+ time)

