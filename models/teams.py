from db import db


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name_team = db.Column(db.String(80), unique=True, nullable=False)
    SG_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    C_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    PF_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    SF_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    PG_player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)



    def to_dict(self):
        return {
            'id': self.id,
            'name_team': self.name,
            'SG_player_id': self.SG_player_id,
            'C_player_id': self.C_player_id,
            'PF_player_id': self.PF_player_id,
            'SF_player_id': self.SF_player_id,
            'PG_player_id': self.Pg_player_id,
        }
