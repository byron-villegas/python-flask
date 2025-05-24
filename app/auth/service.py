import json
from flask import Response, current_app
from werkzeug.exceptions import Unauthorized

def signin(auth):
    unauthorized_response = Response(json.dumps({"statusCode": 401,"message": "Unauthorized"}), 401, mimetype="application/json")

    if (auth["username"] is None or auth["username"] == "") or (auth["password"] is None or auth["password"] == ""):
        raise Unauthorized(response = unauthorized_response)

    users = get_users()

    users_filtered = [item for item in users if item["username"] == auth["username"] and item["password"] == auth["password"]]

    if len(users_filtered) == 0:
        raise Unauthorized(response = unauthorized_response)

    user = users_filtered[0]

    return user

def get_users():
    users = read_users()
    return users

def read_users():
    file_path = current_app.config.get("APP_DIR") + "/data/users.json"

    f = open(file_path, "r")

    users = json.load(f)

    f.close()

    return users
