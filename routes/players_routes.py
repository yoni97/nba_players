from flask import Blueprint, jsonify, request

users_bp = Blueprint('users', __name__)

# from ..models import db


@users_bp.route('/')
def hello_world():  # put application's code here
    return 'Welcome to the NBA leage!'

# @users_bp.route('/players', methods=['GET'])