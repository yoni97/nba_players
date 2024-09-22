from flask import Blueprint, jsonify, request
from services.team_algorithms import get_players_position, compare_teams_ppg, create_new_team, update_team_to_db, \
    delete_team_from_db, checks_teams_exists, get_team_from_db

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('/api/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    name_team = data.get('name_team')
    player_ids = data.get('player_ids')

    if not name_team or len(player_ids) != 5:
        return jsonify({"error": "Team and 5 player IDs numbers are required"}), 400
    players_position = get_players_position(player_ids)
    if len(set(players_position)) != 5:
        return jsonify({"error": "Each position (PG, SG, SF, PF, C) must be represented by one player"}), 400
    new_team = create_new_team(name_team, player_ids)

    if not new_team:
        return jsonify({"error": "Team could not be created"}), 400
    return jsonify(new_team), 201

@teams_bp.route('/api/teams/<team_id>', methods=['PUT'])
def update_team(team_id):
    player_ids  = request.get_json().get('player_ids')
    if not player_ids or len(player_ids) != 5:
        return jsonify({"error": "Exactly 5 player IDs are required"}), 400
    players_positions = get_players_position(player_ids)
    if len(set(players_positions)) != 5:
        return jsonify({"error": "Each position (PG, SG, SF, PF, C) must be represented by one player"}), 400
    updated_team = update_team_to_db(team_id, player_ids)
    if not updated_team:
        return jsonify({"error": "Team couldn't be updated"}), 400
    return jsonify(players_positions), 200


@teams_bp.route('/api/teams/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    result = delete_team_from_db(team_id)
    if result:
        return jsonify({"message": "Team deleted successfully"}), 200
    else:
        return jsonify({"error": "Team not found"}), 404

@teams_bp.route('/api/teams/<int:team_id>', methods=['GET'])
def get_team_details(team_id):
    team = get_team_from_db(team_id)
    if not team:
        return jsonify({"error": "Team not found"}), 404
    return jsonify(team), 200

@teams_bp.route('/api/teams/compare', methods=['GET'])
def compare_teams():
    team_id = request.args.to_dict().values()
    list_team_id = list(team_id)
    if len(list_team_id) < 2 or list_team_id[0] == list_team_id[1]:
        return jsonify({"error": "You need to insert two kinds of teams"}), 400
    teams_exists = checks_teams_exists(list_team_id)
    if not teams_exists:
        return jsonify({'error': 'One or more team not exist'}), 404
    result = compare_teams_ppg(list_team_id)
    return jsonify({"comparison": result}), 200