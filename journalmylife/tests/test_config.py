#!/usr/bin/env python
# -*- coding: utf-8 -*-
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import unittest

from flask import current_app
from flask_testing import TestCase

from journalmylife.journal import app

#unittest.TestCase
class TestAppConfig(TestCase):

#	def setUp(self):
#		pass
	
#	def tearDown(self):
#		pass
		
	def create_app(self):
		app.config.from_object('journalmylife.config.TestingConfig')
		return app
		
	def test_config(self):
		self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
		self.assertTrue(app.config['DEBUG'] is True)
		self.assertFalse(current_app is None)
		self.assertTrue(
			app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///journalmylife_test.db'
		)

class TestDevConfig(TestCase):
	def create_app(self):
		app.config.from_object('journalmylife.config.DevConfig')
		return app

	def test_dev_config(self):
		self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
		self.assertTrue(app.config['DEBUG'] is True)
		self.assertTrue(app.config['BCRYPT_LOG_ROUNDS'] == 4)
		self.assertTrue(
			app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///journalmylife_dev.db'
		)


class TestProductionConfig(TestCase):
	def create_app(self):
		app.config.from_object('journalmylife.config.ProductionConfig')
		return app

	def test_production_config(self):
		self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()