from flask import Flask, render_template, request, redirect, url_for
from waitress import serve
from pysondb import PysonDB
import socket, html

app = Flask(__name__)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

try:
    app.config['SESSION_COOKIE_DOMAIN'] = open("serverName.txt").read()
    app.config['SERVER_NAME'] = IP
except FileNotFoundError:
    pass

db = PysonDB("data.json")

HOST = '0.0.0.0'
PORT = 80
THREADS = 6

def isDoors(data):
    if data['d/w'] == "Doors":
        return True

def isWheals(data):
    if data['d/w'] == "Wheals":
        return True

numDoors = len(db.get_by_query(query=isDoors))
numWheals = len(db.get_by_query(query=isWheals))

@app.route('/data')
def data():
    return render_template("data.html", data=db.get_all())

@app.route('/results')
def results():
    return render_template("results.html", doors=numDoors, wheals=numWheals)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        global numDoors, numWheals
        if not 'd/w' in request.form:
            return redirect("/")
        elif request.form['d/w'] == "Doors":
            numDoors += 1
        elif request.form['d/w'] == "Wheals":
            numWheals += 1
        else:
            return redirect("/")
        
        db.add({
            "name": html.escape(request.form['name']),
            "d/w": request.form['d/w']
        })

        return redirect('/results')

    else:
        return render_template("index.html")

if __name__ == '__main__':
    print(f"connecting with ip: {IP} and port: {PORT}")
    serve(app, host=HOST, port=PORT, threads=THREADS)