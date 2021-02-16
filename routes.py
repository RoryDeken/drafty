
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@app.route('/index.html')
def index(path='/'):
    return redirect('/draftboard', code=301)
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
