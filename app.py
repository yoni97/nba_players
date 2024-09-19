from flask import Flask
from models.players import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

######## first create ########
with app.app_context():
    db.create_all()



if __name__ == '__main__':
    app.run()
