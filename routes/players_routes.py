from flask import Blueprint, jsonify, request
from services.algorithms import get_players_from_db

players_bp = Blueprint('users', __name__)

@players_bp.route('/')
def hello_world():
    return 'Welcome to the NBA league!'

@players_bp.route('/players', methods=['GET'])
def players():
    from services.algorithms import get_players_from_db
    position = request.args.get('position')
    season = request.args.get('season')
    all_players = get_players_from_db(position, season)
    if not all_players:
        return jsonify({'error': 'No players found!'}), 404
    if not position or position not in ['PG', 'SG', 'SF', 'PF', 'C']:
        return jsonify({"error": "Position is required and must be one of PG, SG, SF, PF, C"}), 400
    return jsonify(all_players), 200



