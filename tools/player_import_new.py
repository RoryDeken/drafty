import json

import requests
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Sequence
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://test@localhost/drafty", echo=True)
Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'
    id = Column(String(5), Sequence('player_id_seq'), primary_key=True)
    firstName = Column(String(200))
    lastName = Column(String(200))
    team = Column(String(5))
    position = Column(String(3))
    available = Column(Boolean)

    def __repr__(self):
        return "Player(firstName='%s', lastName='%s', team='%s', position='%s', available='%s')>" % (self.firstName, self.lastName, self.team, self.position, self.available)


Base.metadata.create_all(engine)
# OLD CODE SECTION


# BEGIN OLD CODE
"""
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

# Rewrite this


con = engine.connect()
con.execute("DROP TABLE IF EXISTS players;")
con.execute("DROP TABLE IF EXISTS drafted;")
con.execute(
    "CREATE TABLE IF NOT EXISTS drafted(round varchar(4), id varchar(5), ownedBy varchar(200));")
con.execute("CREATE TABLE IF NOT EXISTS players(firstName varchar(200), lastName varchar(200), team varchar(4), position varchar(3), id varchar(5), available BOOL);")


statement = text(
"""  # """INSERT INTO players(firstName, lastName, team, position, id, available) VALUES(:first_name, :last_name, :team, :position, :id, TRUE)""")
"""
for line in data:
    con.execute(statement, **line)
con.close()
"""
