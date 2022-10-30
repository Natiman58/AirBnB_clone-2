#!/usr/bin/python3
"""
    A script that starts a web application.
"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def HBNB_filters():
    """
        Returns the filtered values of each obj
    """
    cities = storage.all(City).values()
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', **locals())

@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')