#!/usr/bin/python3
"""
    A python script that starts a Flask web application
"""

from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """
        Displays HTML page of all the states in the storage
    """
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def teardown_db(self):
    """
        closes the the current SQLAlchemy session after each request
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
