import json
import pprint

import flask
from flask import jsonify, render_template, request, redirect, url_for, make_response, flash
from flask_cors import CORS

from sqlalchemy import create_engine, insert
from sqlalchemy.sql import text

app = flask.Flask(__name__)
app.secret_key = 'sskfhsjfhskjfhew2342342345%$4%%%'
CORS(app)
app.config["DEBUG"] = True
engine = create_engine("mysql+pymysql://test@localhost/drafty")


def get_all_players():
    con = engine.connect()
    result = con.execute(
        "SELECT * FROM players WHERE ID NOT IN (SELECT id from drafted) LIMIT 15;")
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


# Routes

    # pages

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@app.route('/index.html')
def index(path='/'):
    return render_template('index.html')


@app.route('/page/players/')
@app.route('/page/players.html')
def players_page():
    return render_template('players.html')


@app.route('/login')
@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/basic_table')
@app.route('/basic_table.html')
def basic_table():
    return render_template('basic_table.html')


@app.route('/general')
@app.route('/general.html')
def general():
    return render_template('general.html')


@app.route('/grids')
@app.route('/grids.html')
def grids():
    return render_template('grids.html')


@app.route('/widgets')
@app.route('/widgets.html')
def widgets():
    return render_template('widgets.html')


@app.route('/draftboard/')
@app.route('/draftboard.html')
def draftboard():
    return render_template('draftboard.html')

# API calls


@app.route('/players/')
def get_all():
    return get_all_players()


@app.route('/players/select/<id>', methods=['POST'])
def add_player(id):
    select_player(id)
    return


@app.route('/players/drafted/')
def get_drafted():
    return get_drafted_players()


@app.route('/find/')
def find(player_id):
    player_id = request.args.get('player_id')
    if player_id:
        con = engine.connect()
        result = con.execute(
            "SELECT * FROM players WHERE ID ={};".format(player_id))
        result = result.fetchone()
        first = result[0]
        last = result[1]
        return first + " " + last
    else:
        return "Player not found"


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
app.run(port=8080)
