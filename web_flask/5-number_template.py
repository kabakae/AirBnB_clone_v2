#!/usr/bin/python3
"""
This script starts a Flask web application.
It listens on 0.0.0.0, port 5000, and has the following routes:
- /: displays "Hello HBNB!"
- /hbnb: displays "HBNB"
- /c/<text>: displays "C " followed by the value of the text variable
- /python/(<text>): displays "Python " followed by the value of the text variabl
- /number/<n>: displays "n is a number" only if n is an integer
- /number_template/<n>: displays an HTML page only if n is an integer, with "Number: n" in an H1 tag inside the body
"""

from flask import Flask, render_template
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C ' followed by the value of the text variable"""
    return "C {}".format(escape(text).replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Displays 'Python ' followed by the value of the text variable"""
    return "Python {}".format(escape(text).replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer, with 'Number: n' in an H1 tag inside the body"""
    return render_template('number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
