#!/usr/bin/python3
""" Write script that starts Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Display hello world"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Display C followed by value of text variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
