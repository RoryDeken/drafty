import json

import flask
import requests
from flask import jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to drafty</h1>"


@app.route('/api/v1/', methods=['GET'])
def get_players():
    return jsonify(json.loads(open("data.json", "r").read()))


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
