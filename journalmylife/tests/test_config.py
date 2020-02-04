#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from journalmylife.run import app

class TestAppConfig(unittest.TestCase):

	def setUp(self):
		pass
	
	def tearDown(self):
		pass
		
	def crete_app(self):
		app.config.from_object('')
		return app
		
	def test_config(self):
		self.assertTrue(app.config['DEBUG'] is True)
		self.assertFalse(current_app is None)
		self.assertTrue(
			app.config['SQLALCHEMY_DATABASE_URI'] == ''
		)
		




if __name__ == '__main__':
    unittest.main()