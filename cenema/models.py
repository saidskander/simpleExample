
#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cenema import db


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email


db.create_all()
db.session.commit()
