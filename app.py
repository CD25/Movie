from flask import Flask, render_template, request, redirect
import requests


app = Flask(__name__)


@app.route("/movies", methods=["GET"])
def movies():
    # response = requests.get("https://6452256ebce0b0a0f73dc643.mockapi.io/api/v1/movie")
    return render_template("movie.html")


@app.route("/api/movies", methods=["GET"])
def get_movies():
    return render_template("movie.html")


@app.route("/details", methods=["GET"])
def movieDetail():
    response_id = request.args.get("id")
    return redirect(f"/info?id={response_id}")


@app.route("/info", methods=["GET"])
def movieInfo():
    return render_template("details.html")


@app.route("/emi", methods=["GET"])
def emi():
    return render_template("intrestCal.html")


if __name__ == "__main__":
    app.run(debug=True)
