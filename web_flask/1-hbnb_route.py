#!/usr/bin/python3
"""
Script that starts a Flask web application
1- HBNB
"""
from flask import Flask
app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello_flask():
    """
    Return desired string
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    Return desired string for /hbnb route
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
