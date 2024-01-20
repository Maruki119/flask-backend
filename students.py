from pymongo.mongo_client import MongoClient
from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth

uri = "mongodb+srv://nititornki:nititorn@students.ox3zcvf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["students"]
collection = db["std_info"]

app = Flask(__name__)

#app.config['BASIC_AUTH_USERNAME'] = "username"
#app.config['BASIC_AUTH_PASSWORD'] = "password"
basic_auth = BasicAuth(app)

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

@app.route("/students", methods = ["GET"])
def get_all_students():
    all_students = collection.find()
    return jsonify({"students":[i for i in all_students]})
    
@app.route("/students", methods = ["POST"])
def create_students():
    try:
        data = request.get_json()
        new_student = {
            "_id": data["id"],
            "fullname": data["fullname"],
            "major": data["major"],
            "gpa": data["gpa"]
        }
        collection.insert_one(new_student)
        return jsonify(new_student), 200
    except Exception as e:
        return jsonify({"error":"Cannot create new student"}), 500

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
