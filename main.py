from flask import Flask, render_template
from waitress import serve
import socket

app = Flask(__name__)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

HOST = '0.0.0.0'
PORT = 80
THREADS = 6

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    print(f"connecting with ip: {IP} and port: {PORT}")
    serve(app, host=HOST, port=PORT, threads=THREADS)