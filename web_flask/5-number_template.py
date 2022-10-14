#!/usr/bin/python3
"""
    A python script that starts a flask app
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
        Displays HEllo HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
        Displays HBNB
    """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """
        Displays "C" followed by the value of <text>
        replace '_' with ' '
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def py_text(text="is_cool"):
    """
        Displays Python followed by the default value of <text>
        replace '_' with ' '
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """
        displays n is a number only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html(n):
    """
        displays HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
