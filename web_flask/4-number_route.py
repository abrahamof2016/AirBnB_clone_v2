#!/usr/bin/python3
"""
Script that starts a Flask web application
Is it a number?
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


@app.route('/python/<text>')
def python_is_magic(text):
    """
    Return desired string for /python/<text> route, replace _ with space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/python/')
def python_is_cool():
    """
    Return default string for /python/ route
    """
    text = "is cool"
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def is_it_a_number(n):
    """
    Return a string only if valid int
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
