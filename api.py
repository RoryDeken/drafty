import json
import pprint

import flask
import requests
from flask import jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.sql import text

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

engine = create_engine("mysql+pymysql://test@localhost/drafty")
con = engine.connect()
result = con.execute("SELECT * FROM players;")
result = result.fetchall()
con.close()


d, a = {}, []
for rowproxy in result:
    # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
    for column, value in rowproxy.items():
        # build up the dictionary
        d = {**d, **{column: value}}
    a.append(d)

json_data = json.dumps(a)


@app.route('/', methods=['GET'])
def home():

    return json_data


@app.route('/select/', methods=['POST'])
def add_player():
    return request.data


@app.route('/api/v1/', methods=['GET'])
def get_players():
    return


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
