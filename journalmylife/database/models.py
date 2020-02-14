#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#import jwt
from jose import jwt
import datetime

from journalmylife.journal import app, db, bcrypt

class User(db.Model):
    """ User Model for keeping track of whos who """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    # TODO read up on sqlalchemy keys, and add table addresses!
    # address = -> addresses.id
    birthday = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, password, firstname, lastname, birthday, admin=False):
        self.email = email
        # TODO bcrypt in test/dev phase, need to change to better!
        self.password = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.created = datetime.datetime.now()
        self.admin = admin
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday

    def encode_auth_token(self, user_id):
        """
        Generate the Auth token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string|bytes
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_key'), algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        #except jwt.InvalidTokenError:
        except jwt.JWSError:
            return 'Invalid token. Please log in again.'


class Journal(db.Model):
    """ Journal Model for the journals """
    __tablename__ = "journals"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    journalcontent = db.Column(db.Text, nullable=False)
    #journalowner = db.Column(db.User, nullable=False)
    # ForeignKey("users.id")
    journalcreated = db.Column(db.DateTime, nullable=False)
    journalstatus = db.Column(db.String(255), nullable=False)

    def __init__(self, journalcontent, journalowner, journalcreated, journalstatus):
        self.journalcreated = datetime.datetime.now()
        self.journalcontent = journalcontent
        #self.journalowner = currentUser()
        self.journalstatus = journalstatus

