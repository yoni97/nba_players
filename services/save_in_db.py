from db import db
from models.players import Player
from services.read_from_json import get_nba_stats_games

years = [2022, 2023, 2024]


def save_player_to_database(y2):
    data = get_nba_stats_games(y2)
    if data is None:
        return None
    list_of_players = []
    for player in data:
        player_instance = Player(
            id=player['id'],
            playerName=player['playerName'],
            position=player['position'],
            age=player['age'],
            games=player['games'],
            gamesStarted=player['gamesStarted'],
            minutesPg=player['minutesPg'],
            fieldGoals=player['fieldGoals'],
            fieldAttempts=player['fieldAttempts'],
            fieldPercent=player['fieldPercent'],
            threeFg=player['threeFg'],
            threeAttempts=player['threeAttempts'],
            threePercent=player['threePercent'],
            twoFg=player['twoFg'],
            twoAttempts=player['twoAttempts'],
            twoPercent=player['twoPercent'],
            effectFgPercent=player['effectFgPercent'],
            ft=player['ft'],
            ftAttempts=player['ftAttempts'],
            ftPercent=player['ftPercent'],
            offensiveRb=player['offensiveRb'],
            defensiveRb=player['defensiveRb'],
            totalRb=player['totalRb'],
            assists=player['assists'],
            steals=player["steals"],
            blocks=player["blocks"],
            turnovers=player['turnovers'],
            personalFouls=player['personalFouls'],
            points=player['points'],
            team=player['team'],
            season=player['season'],
            playerId=player['playerId'],
            ATR=player['points'] / player['games'],
            PPG=calculate_ppg_for_player(player['points'], player['games'], data, player['position'])
        )
        db.session.add(player_instance)
        list_of_players.append(player_instance)
    db.session.commit()
    return list_of_players

def commit_all_seasons():
    for year in years:
        save_player_to_database(year)


def calculate_ppg_for_player(points, games, data, position):
    points_per_game = points / games if games > 0 else 0
    average_points = ave_points_position(data, position)
    if average_points == 0:
        return points_per_game
    return points_per_game

def ave_points_position(data, position):
    total_points = 0
    players_in_position = 0

    for player in data:
        if player['position'] == position:
            total_points += player['points']
            players_in_position += player['games']

    average_points = total_points / players_in_position if players_in_position > 0 else 0
    return average_points


# if __name__ == "__main__":
#     from app import app
#     with app.app_context():
        # print(save_to_database(y4))