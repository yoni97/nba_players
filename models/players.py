from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'
    id_table = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    playerName = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer)
    gamesStarted = db.Column(db.Integer)
    minutesPg = db.Column(db.Integer, nullable=False)
    fieldGoals = db.Column(db.Integer)
    fieldAttempts = db.Column(db.Integer)
    fieldPercent = db.Column(db.Float)
    threeFg = db.Column(db.Integer)
    threeAttempts = db.Column(db.Integer)
    threePercent = db.Column(db.Float)
    twoFg = db.Column(db.Integer)
    twoAttempts = db.Column(db.Integer)
    twoPercent = db.Column(db.Float)
    effectFgPercent = db.Column(db.Float)
    ft = db.Column(db.Integer)
    ftAttempts = db.Column(db.Integer)
    ftPercent = db.Column(db.Float)
    offensiveRb = db.Column(db.Integer)
    defensiveRb = db.Column(db.Integer)
    totalRb = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    steals = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    turnovers = db.Column(db.Integer)
    personalFouls = db.Column(db.Integer)
    points = db.Column(db.Integer)
    team = db.Column(db.String)
    season =db.Column(db.Integer)
    playerId = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'playerName': self.playerName,
            'position': self.position,
            'age': self.age,
            'games': self.games,
            'gamesStarted': self.gamesStarted,
            'minutesPg': self.minutesPg,
            'fieldGoals': self.fieldGoals,
            'fieldAttempts': self.fieldAttempts,
            'fieldPercent': self.fieldPercent,
            'threeFg': self.threeFg,
            'threeAttempts': self.threeAttempts,
            'threePercent': self.threePercent,
            'twoFg': self.twoFg,
            'twoAttempts': self.twoAttempts,
            'twoPercent': self.twoPercent,
            'effectFgPercent': self.effectFgPercent,
            'ft': self.ft,
            'ftAttempts': self.ftAttempts,
            'ftPercent': self.ftPercent,
            'offensiveRb': self.offensiveRb,
            'defensiveRb': self.defensiveRb,
            'totalRb': self.totalRb,
            'assists': self.assists,
            'steals': self.steals,
            'blocks': self.blocks,
            'turnovers': self.turnovers,
            'personalFouls': self.personalFouls,
            'points': self.points,
            'team': self.team,
            'season': self.season,
            'playerId': self.playerId,
        }
