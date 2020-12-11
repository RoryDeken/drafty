import json

import requests

url = "https://api.sleeper.app/v1/players/nfl"

r = requests.get(url)

with open('data.json', 'w') as outfile:
    json.dump(json.loads(r.text), outfile)

print("Players synched")
