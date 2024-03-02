from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world_app():
    message = "Hello World from kubernetes!!"
    return message