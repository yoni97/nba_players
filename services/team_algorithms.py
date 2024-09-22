from typing import final

from models.players import Player
from models.teams import Team, db


def get_players_position(player_ids):

    result = []
    try:
        for player_id in player_ids:
            player = Player.query.filter_by(id=player_id).first()
            result.append(player.position)
    except Exception as e:
        print(e)

    return result

def create_new_team(name_team, players_id):
    new_team = Team(
        name_team=name_team,
        SG_player_id=players_id[0],
        C_player_id=players_id[1],
        PF_player_id=players_id[2],
        SF_player_id=players_id[3],
        PG_player_id=players_id[4]
    )
    db.session.add(new_team)
    db.session.commit()
    return new_team.id


def update_team_to_db(team_id, players):
    try:
        team = Team.query.filter_by(id=team_id).first()
        if not team:
            return False
    except Exception as e:
        db.session.rollback()
        return False
    else:
        team.player1_id = players[0]
        team.player2_id = players[1]
        team.player3_id = players[2]
        team.player4_id = players[3]
        team.player5_id = players[4]
        db.session.commit()
        return True

def delete_team_from_db(team_id):
    try:
        team_delete = Team.query.filter_by(id=team_id).first()
        db.session.delete(team_delete)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def details_player(player_id):
    player = Player.query.filter_by(id=player_id).first()
    if not player:
        return {}
    result = {
              'team': player.team,
              'position': player.position,
              'season': player.season,
              'points': player.points,
              'games': player.games,
              'twoPercent': player.twoPercent,
              'threePercent': player.threePercent,
              'ATR': player.ATR,
              'PPG Ratio': player.PPG
              }
    return result

def get_team_from_db(team_id):
    team = Team.query.filter_by(id=team_id).first()
    if not team:
        return False
    result = {
              'name_team': team.name_team,
              'C_player_id': details_player(team.C_player_id),
              'SG_player_id': details_player(team.SG_player_id),
              'PG_player_id': details_player(team.PG_player_id),
              'PF_player_id': details_player(team.PF_player_id),
              'SF_player_id': details_player(team.SF_player_id)
              }
    return result

def checks_teams_exists(team_ids, ):
    for team_id in team_ids:
        if not Team.query.filter_by(id=team_id).first():
            return False
    return True

def compare_teams_ppg(list_team_id):
    my_list = []
    for team_id in list_team_id:
        player = get_team_from_db(team_id)
        final_player = calculate_team_statistics(player)
        my_list.append(final_player)
    sorted_dict = sorted(my_list, key=lambda team: team["PPG"], reverse=True)

    return sorted_dict



def calculate_team_statistics(players):
    points = sum(player['points'] for player in players.values() if isinstance(player, dict))
    twoPercent = sum(player['twoPercent'] for player in players.values()
    if isinstance(player, dict) and 'twoPercent' in player and isinstance(player['twoPercent'], (int, float)))
    threePercent = sum(player['threePercent'] for player in players.values()
    if isinstance(player, dict) and 'threePercent' in player and isinstance(player['threePercent'], (int, float)))
    atr = sum(player['twoPercent'] for player in players.values()
    if isinstance(player, dict) and 'twoPercent' in player and isinstance(player['twoPercent'], (int, float)))
    PPG = sum(player['ATR'] for player in players.values()
    if isinstance(player, dict) and 'ATR' in player and isinstance(player['ATR'], (int, float)))

    return {"name_team": players["name_team"] ,"points": points, "two_percent": twoPercent, "three_percent": threePercent, "ATR": atr,
            "PPG": PPG}
        



