from flask import Flask
from socket import gethostbyname, gethostname

app = Flask(__name__)

@app.route('/')
def hello_world_app():
    hostname = gethostname()
    ip = gethostbyname(hostname)
    message = f"Hello World from {hostname}! IP: {ip}"
    return message
