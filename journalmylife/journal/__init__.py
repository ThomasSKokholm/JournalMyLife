#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object("journalmylife.config")

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

