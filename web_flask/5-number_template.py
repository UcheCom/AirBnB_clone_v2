#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: display “C ” followed by the value of the text
    /python/<text>: display “Python ”, followed by the value of the text
    (replace underscore _ symbols with a space )
    /number/<int:n>: displays 'n is a number' only if <n> is an integer
    /number_template/<int:n>:displays a HTML page only if n is an integer
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """This displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """This displays 'Python' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text='is cool')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """This displays 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """This displays a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0')
