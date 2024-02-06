#!/usr/bin/env python3
"""This module contains a Config class"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """Configures available languages in app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def index() -> str:
    """index page"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)
