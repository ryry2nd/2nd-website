from flask import Flask
from waitress import serve
from Assets import *
import socket

HOST = '0.0.0.0'
PORT = 80
THREADS = 6

app = Flask(__name__)

try:
    prefix = open("rootName.txt").read()
except FileNotFoundError:
    prefix = ""

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

main = MainWebsite(app, prefix)
poll = Poll(app, prefix)

if __name__ == '__main__':
    print(f"connecting with ip: {IP} and port: {PORT}")
    serve(app, host=HOST, port=PORT, threads=THREADS)