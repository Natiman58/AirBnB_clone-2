#!/usr/bin/python3
"""
    a script that starts a Flask web application:
"""

from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states():
    """
        Displays HTML page of all the states in the storage
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all('State'))


@app.teardown_appcontext
def teardown_db(self):
    """
        closes the the current SQLAlchemy session after each request
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
