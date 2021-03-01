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


class MaraudeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    volunteer_0 = db.Column(db.Integer, nullable=False)
    volunteer_1 = db.Column(db.Integer, nullable=True)
    volunteer_2 = db.Column(db.Integer, nullable=True)
    volunteer_3 = db.Column(db.Integer, nullable=True)


db.create_all()  # Initialize the database
