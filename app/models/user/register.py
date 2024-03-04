from app import db

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key-True)
    type_of_ticket = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    type_of_ticket = db.Column(db.string(50), nullable=False)
    