from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os.path import join, dirname, abspath

app = Flask(__name__)

BASE_DIR = dirname(abspath(__file__))
db_path = join(BASE_DIR, "database.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
db = SQLAlchemy(app)


class VolunteerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # primary_key means unique
    forename = db.Column(db.String(30), nullable=False)  # nullable=False means required
    surname = db.Column(db.String(30), nullable=False)  # 30 is max length


class HomelessModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    forename = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=True)


class MaraudeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=True)
    day = db.Column(db.Integer, nullable=True)


class ParticipationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    volunteer_id = db.Column(db.Integer, nullable=False)
    maraude_id = db.Column(db.Integer, nullable=False)


class EncounterModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    homeless_id = db.Column(db.Integer, nullable=False)
    maraude_id = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    minute = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(200), nullable=False)


db.create_all()  # Initialize the database
