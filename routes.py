
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/players/')
def get_all():
    return get_all_players()


@app.route('/players/select/<id>', methods=['POST'])
def add_player(id):
    select_player(id)
    return "Player with id# {} added".format(id)


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
