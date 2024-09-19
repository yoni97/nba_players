from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name_team = db.Column(db.String(100), nullable=False)
    id_of_player = db.Column(db.PickleType, nullable=False)
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(80), unique=True, nullable=False)
    # SG_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    # C_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    # PF_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    # SF_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    # Pg_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    #
    # players = db.relationship('Player', backref='team', lazy='dynamic')


    def to_dict(self):
        return {
            'id': self.id,
            'name_team': self.name_team,
            'id_of_player': self.id_of_player
        }
    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'SG_player_id': self.SG_player_id,
    #         'C_player_id': self.C_player_id,
    #         'PF_player_id': self.PF_player_id,
    #         'SF_player_id': self.SF_player_id,
    #         'Pg_player_id': self.Pg_player_id,
    #         'players': self.players,
    #     }
