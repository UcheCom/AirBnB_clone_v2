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


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays a HTML page of State objects present in DBStorage
    States are sorted by name
    """

    states = storage.all('State')
    return render_template("7-states_list.html", Table="States", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0')
