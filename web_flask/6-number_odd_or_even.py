#!/usr/bin/python3
"""
Script that starts a Flask web application
6- Odd or even?
"""
from flask import Flask, render_template
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Displays an html page only if number is int
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_template_odd_or_even(n):
    """
    Displays an html page only if number is int odd or even
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
