import requests
# from app import app
from models.players import Player, db

years = [2022, 2023, 2024]
y3 = 2023
y2 = 2022
y4 = 2024


def get_nba_stats_games(y2):
    url_link = f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={y2}&&pageSize=1000'
    response = requests.get(url_link)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Failed to retrieve data: {response.status_code}"


def save_to_database(y2):
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
            ATR = player['points'] / player['games']
        )
        db.session.add(player_instance)
        list_of_players.append(player_instance)
    db.session.commit()
    return list_of_players

# def commit_all_seasons():
#     for year in years:
#         save_to_database(year)



# if __name__ == "__main__":
#     with app.app_context():
#         print(save_to_database(y4))
