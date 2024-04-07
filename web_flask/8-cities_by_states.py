#!/usr/bin/python3
"""Query the state frm a database on run it flask"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """State the states list"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Close cuurent SQLALchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")