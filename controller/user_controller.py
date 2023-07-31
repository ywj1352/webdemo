from flask import jsonify, current_app, request
from . import api
from config import user_config


@api.route('/hello-config', methods=['GET'])
def hello_config():
    name = request.args.get('name')
    password = request.args.get('password')
    items = [
        {
            "username": name,
            "password": password,
            "config_username": user_config.get_user_name(),
            "config_password": user_config.get_password()
        }
    ]
    return jsonify(items)


@api.route("/hello-database", methods=['GET'])
def hello_database():
    return "null"
