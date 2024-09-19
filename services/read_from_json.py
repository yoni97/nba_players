import json
import requests
from models.players import Player, db

year1 = 2022
year2 = 2023
year3 = 2024



def get_nba_stats_games(year3):
    url_link = f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year3}&&pageSize=1000'
    response = requests.get(url_link)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Failed to retrieve data: {response.status_code}"
print(get_nba_stats_games(year3))

def save_to_database():
    data = get_nba_stats_games(year3)
    if data is None:
        return None
    for player in data:
        list_of_players = Player(
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
            playerId=player['playerId']
    )
        db.session.add(data)
        db.commit()
        return list_of_players
print(save_to_database())

# print(get_nba_stats_games(API_LINK_2023))
# print(get_nba_stats_games(API_LINK_2022))