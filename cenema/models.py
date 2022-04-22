
#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cenema import db


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    def __repr__(self):
        return '<Booking %r>' % self.email


db.create_all()
db.session.commit()
