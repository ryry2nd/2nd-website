from mysite.wsgi import application as app
from waitress import serve
import socket

HOST = '0.0.0.0'
PORT = 80
THREADS = 6

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

if __name__ == '__main__':
    print(f"connecting with ip: {IP} and port: {PORT}")
    serve(app, host=HOST, port=PORT, threads=THREADS)