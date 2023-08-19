"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_bcrypt import Bcrypt

api = Blueprint('api', __name__)
app = Flask(__name__)
bcrypt = Bcrypt(app)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def create_user():
    email = request.json.get("email")
    password = request.json.get("password")
    secure_password = bcrypt.generate_password_hash(password, 10).decode("utf-8")
    #new_user = User(email=data.email, password=data.password)
    new_user = User()
    new_user.email = email
    new_user.password = secure_password
    new_user.is_active = True
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg":"Usuario registrado"}), 201