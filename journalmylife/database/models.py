#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import datetime

from journal import app, db#, bcrypt

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

    def __init__(self, email, password, admin=False, firstname, lastname, birthday):
        self.email = email
        # TODO bcrypt in test/dev phase, need to change to better!
        self.password = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.created = datetime.datetime.now()
        self.admin = admin
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday



