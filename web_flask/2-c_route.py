#!/usr/bin/python3
"""
Script that starts a Flask web application
2- C is fun!
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


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Return desired string for /c/<text> route, replace _ with space
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
