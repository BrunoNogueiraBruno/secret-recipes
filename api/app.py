import uuid
from flask import Flask, flash, request, session
from flask_cors import CORS
from core.login.login import Login
from core.login.login_service import LoginService

from core.user.user_service import userService

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
CORS(app, supports_credentials=True)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    service = LoginService()

    username = data["username"]
    password = data["password"]

    obj_login = Login(username, password)

    try:
        service.autenticar(obj_login)
        session['user'] = username
        return {"user": session.get("user")}, 200

    except ValueError as e:
        flash(str(e), "error")
        return {"error": "Credenciais inválidas"}, 401


@app.route("/users", methods=["GET"])
def users():
    return {"users": [u.to_dict() for u in userService.list_users()]}, 200

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