#!/usr/bin/python3
# A python script that starts a flask app

from flask import Flask
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
        Displays "C" followed by the value of <text>
        replace '_' with ' '
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is_cool"):
    """
        Displays Python followed by the default value of <text>
        replace '_' with ' '
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
