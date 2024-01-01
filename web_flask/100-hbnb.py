#!/usr/bin/python3
""" Starts a  Flask web application
Application must be listening on 0.0.0.0, port 5000
Routes:
    /hbnb: displays HTML pages
"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays a HTML page state, cities, places and amenities
    """

    places = storage.all('Place')
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template("100-hbnb.html", states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0')
