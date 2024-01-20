from pymongo.mongo_client import MongoClient
from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = "username"
app.config['BASIC_AUTH_PASSWORD'] = "password"
basic_auth = BasicAuth(app)

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
