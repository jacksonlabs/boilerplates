from flask import Flask
from flask import jsonify, make_response
import config
import os

app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello World!")
    return "Hello World!"

@app.route('/env')
def environment():
    data = {
        "FLASK_ENV": os.environ['FLASK_ENV'],
        "MODE": os.environ['MODE'],
        "DEBUG_MODE": os.environ['DEBUG_MODE'],
    }
    return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.run()
