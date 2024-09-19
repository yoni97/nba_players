from flask import Blueprint, jsonify, request

teams_bp = Blueprint('teams', __name__)

from models.teams import db, Team
from models.players import db, Player

teams_bp = Blueprint('teams', __name__)


@teams_bp.route('/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    name_team = data.get('name_team')
    ids_player = data.get('id_of_player')
    if not name_team:
        return jsonify({"error": "Team name is required!"}), 400
    if not isinstance(ids_player, list) or len(ids_player) < 5:
        return jsonify({"error": "You must provide at least 5 player IDs!"}), 400
    positions = {'PG': 0, 'SG': 0, 'SF': 0, 'PF': 0, 'C': 0}
    players = Player.query.filter(Player.id.in_(ids_player)and Player.team).all()
    if len(players) < 5:
        return jsonify({"error": "Not all player IDs are valid!"}), 400
    for player in players:
        positions[player.position] += 1
    if any(count < 1 for count in positions.values()):
        return jsonify({"error": "Must have at least one player in each position!"}), 400
    new_team = Team(name_team=name_team, ids_player=ids_player)
    db.session.add(new_team)
    db.session.commit()

    return jsonify({"message": "Team created successfully!",
                    "team": {"id": new_team.id, "name_team": new_team.name_team,
                             "id_of_player": new_team.id_of_player}}), 201
