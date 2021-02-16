import json

import requests
from models import *

url = "https://api.sleeper.app/v1/players/nfl"

r = requests.get(url)
players_returned = json.loads(r.text)
players = []
active_players = []

for player in players_returned:
    players.append(players_returned[player])

for player in players:
    if player["active"] == True and player["position"] == 'QB' or player["position"] == 'RB' or player["position"] == 'WR' or player["position"] == 'TE' or player["position"] == 'DEF' or player["position"] == 'K':
        if 'status' in player.keys():
            if player['status'] != 'Inactive':
                active_players.append(player)
        else:
            active_players.append(player)

players = sorted(active_players, key=lambda k: k['last_name'])
data = []
for player in players:
    data.append(
        {
            'first_name': player['first_name'],
            'last_name': player['last_name'],
            'team': str(player['team']),
            'position': player['position'],
            'id': str(player['player_id'])

        }
    )

for d in data:
    current = Player(id=d['id'], firstName=d['first_name'], lastName=d['last_name'],
                     team=d['team'], position=d['position'], available=True)
    session.add(current)

session.commit()
