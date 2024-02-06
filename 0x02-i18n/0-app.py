#!/usr/bin/env python3
"""This module contains a basic flask application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """index page"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
