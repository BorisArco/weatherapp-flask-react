from logging import debug
import datetime as dt
import requests, json
from flask import Flask

app = Flask(__name__)


# Members api route


@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route("/city")
def city():
    BASE_URL = " http://api.weatherapi.com/v1/"
    API_KEY = open("api_key", "r").read()
    CITY = "London"
    url = BASE_URL + "current.json?key=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    return response


if __name__ == "__main__":
    app.run(debug=True)
