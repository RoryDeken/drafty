import flask
from flask import jsonify, render_template, request, redirect, url_for, make_response, flash
from flask import current_app as app
from .models import db, Player, Drafted


def get_all_players():
    players = []
    for instance in db.session.query(Player).order_by(Player.rank.asc()):
        print(type(instance.rank))
        players.append(
            {
                "id": instance.id,
                "espnId": instance.espnId,
                "rank": instance.rank,
                "firstName": instance.firstName,
                "lastName": instance.lastName,
                "team": instance.team,
                "position": instance.position,
                "available": instance.available
            }
        )
    return jsonify(players)


def get_drafted_players():
    drafted_players = []
    for instance in db.session.query(Drafted):
        drafted_players.append(
            {
                "id": instance.id,
                "firstName": instance.firstName,
                "lastName": instance.lastName,
                "team": instance.team,
                "position": instance.position,
                "ownedBy": instance.ownedBy,
            }
        )
    return jsonify(drafted_players)


def select_player(id):
    selected_player = get_player(id)
    new_drafted_player = Drafted(
        id=selected_player.id,
        firstName=selected_player.firstName,
        lastName=selected_player.lastName,
        team=selected_player.team,
        position=selected_player.position,
        round=1,
        ownedBy='N/A'
    )
    db.session.add(new_drafted_player)
    return jsonify('Player added'), 200, {'ContentType': 'application/json'}


def get_player(id):
    player = Player.query.filter(Player.id == id).first()
    db.session.commit()
    return player

# Routes

    # pages


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
@app.route('/')
def index():
    return 'hello'
    # return render_template('index.html')


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


@app.route('/test')
def test_route():
    return get_all_players()


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
    return select_player(id)


@app.route('/players/drafted/')
def get_drafted():
    return get_drafted_players()


@app.route('/players/search')
def search_player(player_id=''):
    arg = request.args.get('player_id')
    if arg:
        player = get_player(arg)
        if player:
            player = {
                "name": player.firstName + " " + player.lastName,
                "team": player.team,
                "position": player.position
            }
            return jsonify(player)
        else:
            return "Player ID not found"
    else:
        return "Please enter a player ID"
