#!/usr/bin/python3
""" Starts a  Flask web application
Application must be listening on 0.0.0.0, port 5000
Routes:
    /states_list: displays a HTML page of State objects present in DBStorage
"""

import sqlalchemy
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays a HTML page of State objects present in DBStorage
    States/cities are sorted by name
    """

    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0')
