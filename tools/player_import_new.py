import json

import requests
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base

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

engine = create_engine("mysql+pymysql://test@localhost/drafty", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Player(Base):
    __tablename__ = 'players'
    id = Column(String(5), primary_key=True)
    firstName = Column(String(200))
    lastName = Column(String(200))
    team = Column(String(5))
    position = Column(String(3))
    available = Column(Boolean)

    def __repr__(self):
        return "Player(id='%s', firstName='%s', lastName='%s', team='%s', position='%s', available='%s')>" % (self.id, self.firstName, self.lastName, self.team, self.position, self.available)


class Drafted(Base):
    __tablename__ = 'drafted'
    id = Column(String(5), primary_key=True)
    firstName = Column(String(200))
    lastName = Column(String(200))
    team = Column(String(5))
    position = Column(String(3))
    round = Column(Integer())
    ownedBy = Column(String(200))

    def __repr__(self):
        return "Player(id='%s', firstName='%s', lastName='%s', team='%s', position='%s', round='%s', ownedBy='%s')>" % (self.id, self.firstName, self.lastName, self.team, self.position, self.round, self.ownedBy)


Base.metadata.create_all(engine)
session = Session()
for d in data:
    current = Player(id=d['id'], firstName=d['first_name'], lastName=d['last_name'],
                     team=d['team'], position=d['position'], available=True)
    session.add(current)

session.commit()
