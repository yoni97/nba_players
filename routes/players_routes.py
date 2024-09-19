from flask import Blueprint, jsonify, request

from app import app

users_bp = Blueprint('users', __name__)

# from ..models import


@users_bp.route('/')
def hello_world():  # put application's code here
    return 'Welcome to the NBA leage!'

@users_bp.route('/players', methods=['GET'])
def players():

    all_players = players.query.all()
    return jsonify(all_players)

# @users_bp.route('/players?position={position}&season={season}', methods=['GET'])
# def get_players():
