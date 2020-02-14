#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import datetime

from journalmylife.journal import db
from journalmylife.database.models import User
from journalmylife.tests.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test',
            firstname='Test',
            lastname='Tester',
            birthday=datetime.datetime.utcnow() - datetime.timedelta(days=6570, seconds=5)
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        print(auth_token)
        self.assertTrue(isinstance(auth_token, bytes))

if __name__ == '__main__':
    unittest.main()