from flask import Flask, render_template, request, redirect
from waitress import serve
import socket, json

app = Flask(__name__)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

try:
    data = json.load(open("data.json"))
except FileNotFoundError:
    data = {"Doors": 0, "Wheals": 0}
    json.dump(data, open("data.json", "w"))

HOST = '0.0.0.0'
PORT = 80
THREADS = 6

numDoors = data["Doors"]
numWheals = data["Wheals"]

@app.route('/data')
def data():
    return render_template("data.html", doors=numDoors, wheals=numWheals)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        global numDoors, numWheals
        if request.form['d/w'] == "Doors":
            numDoors += 1
        elif request.form['d/w'] == "Wheals":
            numWheals += 1

        with open('data.json', 'w') as f:
            json.dump({"Doors": numDoors, "Wheals": numWheals}, f)

        return redirect('/data')
    else:
        return render_template("index.html")

if __name__ == '__main__':
    print(f"connecting with ip: {IP} and port: {PORT}")
    serve(app, host=HOST, port=PORT, threads=THREADS)