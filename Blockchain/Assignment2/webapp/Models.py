from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table

db = SQLAlchemy()

class Players(db.Model):

    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(100), nullable=False)
    randomseed = db.Column(db.String(64),nullable=False)
