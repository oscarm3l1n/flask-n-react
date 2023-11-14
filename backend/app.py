from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/home", methods=["GET"])
def home():
    response = {"data": 3}
    return jsonify(response), 200
