import click
import requests
import flask
from flask import current_app as app
from .models import db, Player, Drafted


@app.cli.command('import')
def importplayers():

    print('Starting import...')
    url = "https://api.sleeper.app/v1/players/nfl"

    r = requests.get(url)
    players_returned = flask.json.loads(r.text)
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
        if 'espn_id' not in player:
            player['espn_id'] = 'N/A'

        if 'search_rank' not in player:
            player['search_rank'] = 999999
        else:
            if player['search_rank'] is None:
                player['search_rank'] = 999999

    players = sorted(active_players, key=lambda k: k['last_name'])

    Player.query.delete()
    Drafted.query.delete()
    data = []
    for player in players:
        data.append(
            Player(
                id=player['player_id'],
                espnId=player['espn_id'],
                rank=int(player['search_rank']),
                firstName=player['first_name'],
                lastName=player['last_name'],
                team=str(player['team']),
                position=player['position'],
                available=True
            )
        )

    db.session.add_all(data)
    db.session.commit()
    print('Import complete!!!')
