"""
This file contains the Users table definition.
"""
from .base import db
import hashlib


class Users(db.Model):
    """
    Users table
    """
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    usertype = db.Column(db.String(255), unique=False, nullable=False)
    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, uid, username, password, usertype,
                 first_name, last_name):
        self.uid = uid
        self.username = username
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self.usertype = usertype
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User {}>'.format(self.username)
