from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship('Player', backref='team', lazy='dynamic')


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
