import requests
response = requests.get('https://www.cerosilva.com')
print(response)



url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

querystring = {"q":"get:new7:US","p":"1","t":"ns","st":"adv"}

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "2c31d846abmsh4ae947e8dc39a84p167729jsn26f549e59e3c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
