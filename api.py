import json

import flask
import requests
from flask import escape, jsonify
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


app.run()
