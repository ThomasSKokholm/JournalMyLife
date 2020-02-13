#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ.get('DB_HOST')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "sqlite:///journalmylife.db"

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USER, DB_PASSWORD, DB_HOST, 'journal')
    #SQLALCHEMY_DATABASE_URI = "sqlite:///journalmylife.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #BCRYPT_LOG_ROUNDS = 13

class DevConfig(BaseConfig):
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = "sqlite:///journalmylife_dev.db"

class TestingConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///journalmylife_test.db"# +"_test"

class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USER, DB_PASSWORD, DB_HOST, 'journal')


    

