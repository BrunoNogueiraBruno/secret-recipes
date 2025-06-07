import uuid
from flask import Flask, request, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
CORS(app, supports_credentials=True)

db_user = {
    "username": "bruno",
    "password": "123"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    if username == db_user["username"] and password == db_user["password"]:
        session["user"] = data["username"]
        return {"user": session.get("user")}, 200
    
    else:
        return {"error": "Credenciais inválidas"}, 401

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return '', 204

@app.route('/me', methods=['GET'])
def me():
    if 'user' in session:
        return {"authenticated": True, "user": session['user']}
    else:
        return {"authenticated": False}, 401