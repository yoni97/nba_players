from models.players import Player

def get_players_from_db(position, season=None):
    if season:
        query = Player.query.filter_by(position=position, season=season).all()
    else:
        query = Player.query.filter_by(position=position).all()

    result = [{'playerName': player.playerName,
               'team': player.team,
               'position': player.position,
               'season': player.season,
               'points': player.points,
               'games': player.games,
               'twoPercent': player.twoPercent,
               'threePercent': player.threePercent,
               'ATR': player.ATR,
               'PPG Ratio': player.PPG}
              for player in query]
    return result
