from datetime import datetime
from flask import Flask
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True) 
    author = db.Column(db.String(30))
    date = db.Column(db.DateTime, default=func.now())
    id_janr = db.Column(db.Integer, db.ForeignKey('janr.id', ondelete ="SET NULL"))
    janr = relationship('janr', back_populates='book')
    
    def __repr__(self):
        return f"Books(name={self.name!r})"

class janr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(20))
    book = relationship('Books', back_populates='janr')
    
