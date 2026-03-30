from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    senha = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='user')

