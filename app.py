import users_api
from init_db import create_tables
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return "The API works"


@app.route("/users", methods=["GET"])
def get_users():
    users = users_api.get_users()
    return jsonify(users)


@app.route("/user", methods=["POST"])
def insert_user():
    user_details = request.get_json()
    name = user_details["name"]
    result = users_api.insert_user(name)
    return jsonify(result)


@app.route("/user", methods=["PUT"])
def update_user():
    user_details = request.get_json()
    id = user_details["id"]
    name = user_details["name"]
    result = users_api.update_user(id, name)
    return jsonify(result)


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    result = users_api.delete_user(id)
    return jsonify(result)


@app.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    user = users_api.get_by_id(id)
    return jsonify(user)


if __name__ == "__main__":
    create_tables()
    app.run(host="0.0.0.0", port=8000, debug=True)
