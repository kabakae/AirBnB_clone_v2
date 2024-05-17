#!/usr/bin/python3
"""
This script starts a Flask web application.
It listens on 0.0.0.0, port 5000, and has two routes:
- /: displays "Hello HBNB!"
- /hbnb: displays "HBNB"
"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C ' followed by the value of the text variable"""
    return "C {}".format(escape(text).replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
