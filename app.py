from flask import Flask
from models.players import db
from flask_migrate import Migrate, upgrade

from routes.players_routes import players_bp
from routes.team_routes import teams_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
######## first create ########

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

with app.app_context():
    upgrade()
app.register_blueprint(players_bp)
app.register_blueprint(teams_bp)

if __name__ == '__main__':
    app.run(debug=True)
