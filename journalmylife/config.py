#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ.get('DB_HOST')
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USER, DB_PASSWORD, DB_HOST, 'kitos')
	
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	BCRYPT_LOG_ROUNDS = 13