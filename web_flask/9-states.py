#!/usr/bin/python3
""" Starts a  Flask web application
Application must be listening on 0.0.0.0, port 5000
Routes:
    /states: displays a HTML page of State objects present in DBStorage
    /states/<id>: display a HTML page: (inside the tag BODY)
"""

from models import *
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """Displays a HTML page of State and city objects present in DBStorage
       sorted by name
    """
    states = storage.all('State')
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0')
