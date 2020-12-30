import json

import requests
from sqlalchemy import create_engine

'''
    engine = create_engine("mysql+pymysql://test@localhost/drafty")

    con = engine.connect()  # Connect to the MySQL engine
result = con.execute("DROP TABLE IF EXISTS players;")
con.close()

'''
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
count = 0


for player in players:
    print(player['first_name'] + " " + player['last_name'] +
          " " + player['position'] + " " + str(player['team']))
    count = count + 1
print("There are " + str(count) + " active players.")
with open("data.json", "w") as outfile:
    json.dump(players, outfile)
