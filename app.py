from flask import Flask, render_template, request, jsonify
from flaskwebgui import FlaskUI

from helper import load_data, look_up

exoplanets = load_data("static/")
data = exoplanets[0]
columns = exoplanets[1]

app = Flask(__name__) 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.args.get("id")
        result = look_up(data,query)
        render_template("search.html", planets=result)
    q = request.args.get("q")
    if q:
        if q[-5:] == "by_id":
            result = look_up(data,q[:-5], True)
            render_template("search.html",planets=result)
        else:
            result = look_up(data, q)
    else:
        result = []
    return jsonify(result)
            
"""
@app.route("/search/<int: id>")
def search_by_id(id):
    planets = search(data, id, True)
    render_template("search.html",planets=planets)
"""