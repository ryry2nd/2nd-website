from flask import render_template, request, redirect, Flask
from pysondb import PysonDB
import html

db = PysonDB("data.json")

class Poll:
    def __init__(self, app:Flask, prefix: str):
        self.prefix = prefix
        self.numDoors = len(db.get_by_query(query=self.isDoors))
        self.numWheals = len(db.get_by_query(query=self.isWheals))

        self.initPoll(app)


    def isDoors(self, data):
        if data['d/w'] == "Doors":
            return True

    def isWheals(self, data):
        if data['d/w'] == "Wheals":
            return True

    def initPoll(self, app: Flask):
        @app.route('/poll/data')
        def data():
            return render_template("data.html", data=db.get_all(), prefix=self.prefix)

        @app.route('/poll/results', methods=['POST', 'GET'])
        def results():
            if request.method == 'POST':
                if not 'd/w' in request.form:
                    return redirect(self.prefix)
                elif request.form['d/w'] == "Doors":
                    self.numDoors += 1
                elif request.form['d/w'] == "Wheals":
                    self.numWheals += 1
                else:
                    return redirect(self.prefix)
                
                db.add({
                    "name": html.escape(request.form['name']),
                    "d/w": request.form['d/w']
                })
            
            return render_template("results.html", doors=self.numDoors, wheals=self.numWheals, prefix=self.prefix)

        @app.route('/poll')
        def poll():
            return render_template("poll.html", prefix=self.prefix)