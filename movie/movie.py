from flask import Flask, request, jsonify, make_response
import json
import sys
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3200
HOST = "0.0.0.0"

with open("{}/databases/movies.json".format("."), "r") as jsf:
    movies = json.load(jsf)["movies"]

# root message
@app.route("/", methods=["GET"])
def home():
    return make_response(
        "<h1 style='color:blue'>Welcome to the Movie service!</h1>", 200
    )

@app.route("/json", methods=["GET"])
def get_json():
    res = make_response(jsonify(movies), 200)
    return res

@app.route("/movies/<movie_id>", methods=["GET"])
def get_movie_byid(movie_id):
    for movie in movies:
        if str(movie["id"]) == str(movie_id):
            res = make_response(jsonify(movie), 200)
            return res
    return make_response(jsonify({"error": "Movie ID not found"}), 400)

@app.route("/moviesbytitle", methods=["GET"])
def get_movie_bytitle():
    json = ""
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["title"]) == str(req["title"]):
                json = movie

    if not json:
        res = make_response(jsonify({"error": "movie title not found"}), 400)
    else:
        res = make_response(jsonify(json), 200)
    return res

@app.route("/movies/<movie_id>", methods=["POST"])
def create_movie(movie_id):
    req = request.get_json()

    for movie in movies:
        if str(movie["id"]) == str(movie_id):
            return make_response(jsonify({"error": "movie ID already exists"}), 409)

    movies.append(req)
    res = make_response(jsonify({"message": "movie added"}), 200)
    return res

@app.route("/movies/<movie_id>/<rate>", methods=["PUT"])
def update_movie_rating(movie_id, rate):
    for movie in movies:
        if str(movie["id"]) == str(movie_id):
            movie["rating"] = int(rate)
            res = make_response(jsonify(movie), 200)
            return res

    res = make_response(jsonify({"error": "movie ID not found"}), 201)
    return res

@app.route("/movies/<movie_id>", methods=["DELETE"])
def del_movie(movie_id):
    for movie in movies:
        if str(movie["id"]) == str(movie_id):
            movies.remove(movie)
            return make_response(jsonify(movie), 200)

    res = make_response(jsonify({"error": "movie ID not found"}), 400)
    return res

if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT, debug=True)
