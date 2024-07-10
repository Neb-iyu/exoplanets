from flask import Flask, render_template, request, jsonify
from flaskwebgui import FlaskUI

from helper import load_data, look_up, link

exoplanets = load_data("static/")
data = exoplanets[0]
columns = exoplanets[1]

app = Flask(__name__) 

#custom filter for jinja
app.jinja_env.filters["link"] = link
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("input")
        if query:
            result = look_up(data,query)
        return render_template("search.html", planets=result)
    q = request.args.get("q")
    if q:
        if q[-5:] == "by_id":
            result = look_up(data, q[:-5], True)
            return render_template("search.html", planet=result)
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