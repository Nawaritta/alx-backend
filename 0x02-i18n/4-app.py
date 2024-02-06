#!/usr/bin/env python3
"""This module contains get_locale method"""
from flask import Flask, render_template, request
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
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """Matches the locale with the supported languages"""

    locale = request.args.get('locale')
    if locale:
        if locale in app.config["LANGUAGES"]:
            return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run(debug=True)
