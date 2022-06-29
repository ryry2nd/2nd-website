from sys import prefix
from flask import render_template, Flask
import html

class MainWebsite:
    def __init__(self, app:Flask, prefix: str):
        self.prefix = prefix

        self.initPoll(app)

    def initPoll(self, app):
        @app.route("/")
        def index():
            return render_template("index.html", prefix=self.prefix)