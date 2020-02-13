#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_testing import TestCase

from journalmylife.journal import app, db


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('journalmylife.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()
	
    def tearDown(self):
        db.session.remove()
        db.drop_all()

