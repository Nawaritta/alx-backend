#!/usr/bin/env python3
"""This module contains get_user and before_request methods"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Configures available languages in app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def index():
    """index page"""
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """Matches the locale with the supported languages"""

    locale = request.args.get('locale')
    if locale:
        if locale in app.config["LANGUAGES"]:
            return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """ returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed."""
    id = request.args.get('login_as')
    return users.get(int(id), None)


@app.before_request
def before_request():
    """executed before all other functions"""
    user = get_user()
    if user:
        g.user = user


if __name__ == '__main__':
    app.run(debug=True)