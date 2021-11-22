from .__init__ import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    listings = db.relationship('Listing')


# db will consist of address information, price
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    type = db.Column(db.String(150))
    photo = db.Column(db.String(150))
    address1 = db.Column(db.String(150))
    address2 = db.Column(db.String(150))
    consent = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))