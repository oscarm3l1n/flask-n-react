from flask import Flask, jsonify, render_template
from flask_cors import CORS


static_files = "../frontend/out"
app = Flask(
    __name__,
    static_folder="/Users/oscar.melin/dev/flask-n-react/frontend/out",
    static_url_path="",
    template_folder="../frontend/out",
)
CORS(app)


@app.route("/")
def index_redit():
    return render_template("index.html")


@app.route("/home", methods=["GET"])
def home():
    response = {"data": 3}
    return jsonify(response), 200
