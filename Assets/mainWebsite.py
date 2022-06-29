from flask import render_template, Flask

class MainWebsite:
    def __init__(self, app:Flask, prefix: str):
        self.prefix = prefix

        self.initPoll(app)

    def initPoll(self, app: Flask):
        @app.route("/")
        def index():
            return render_template("index.html", prefix=self.prefix)