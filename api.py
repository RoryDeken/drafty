import json
import pprint

import flask
import requests
from flask import jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, insert
from sqlalchemy.sql import text

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
engine = create_engine("mysql+pymysql://test@localhost/drafty")


def get_all_players():
    con = engine.connect()
    result = con.execute(
        "SELECT * FROM players WHERE ID NOT IN (SELECT id from drafted);")
    result = result.fetchall()
    con.close()
    d, a = {}, []
    for rowproxy in result:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)

    return json.dumps(a)


def get_drafted_players():
    con = engine.connect()
    drafted = con.execute("SELECT * FROM drafted;")
    drafted = drafted.fetchall()
    con.close()
    d, a = {}, []
    for rowproxy in drafted:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)

    return json.dumps(a)


def select_player(player):
    con = engine.connect()
    data = ({"id": player, "round": 1, "ownedBy": "Team 1"},)
    statement = text(
        """INSERT INTO drafted(id, round, ownedBy) VALUES(:id, :round, :ownedBy)""")
    for line in data:
        con.execute(statement, **line)
    con.close()


@app.route('/', methods=['GET'])
def home():

    return get_all_players()


@app.route('/select/', methods=['POST'])
def add_player():
    player = json.loads(request.data)
    select_player(player)
    return "Player with id# {} added".format(player)


@app.route('/drafted/', methods=['GET'])
def get_players():
    return get_drafted_players()


"""
Routes
     GET/
        . GET Available players
        . GET Drafted players/draft board
        . GET Teams with current roster
            * Team roster structure

    POST/
        . Add player to Team/remove from Available players
        
Admin things
    . Ability to create an account/Team
        * Different roles commisoner vs owner
    . Create a league draft with time and number of teams
        * Allow league settings, roster type (2WR/2RB etc), scoring type (PPR/Standard etc)
        * Allow commisoner to pause/start and edit picks
        * Allow snake format for draft
        * Allow ability for teams to be forced to draft their starting lineup first
"""
app.run()
