#!/usr/bin/python3
"""Run a flask app that returns Hello HBNB"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return hello NMBB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return hbnb"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    """Configure C is Fun"""
    text = text.replace('_', ' ')
    value = 'C {}'.format(text)
    return value


if __name__ == "__main__":
    app.run(host="0.0.0.0")