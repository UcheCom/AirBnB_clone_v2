#!/usr/bin/python3
""" Starts a  Flask web application
Application must be listening on 0.0.0.0, port 5000
Routes:
    /hbnb_filters: displays a HTML page like 6-index.html
"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page like 6-index.html
    """

    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0')
