#!/usr/bin/python3
"""
This script starts a Flask web application.
It listens on 0.0.0.0, port 5000, and has the following routes:
- /: displays "Hello HBNB!"
- /hbnb: displays "HBNB"
- /c/<text>: displays "C " followed by the value of the text variable
- /python/<text>: displays "Python " followed by the value of the text variable (default: "is cool")
- /number/<n>: displays "n is a number" only if n is an integer
- /number_template/<n>: displays an HTML page only if n is an integer
- /number_odd_or_even/<n>: displays an HTML page only if n is an integer
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
    """Displays an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if n is an integer"""
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

