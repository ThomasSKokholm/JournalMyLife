#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
import coverage

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

COV = coverage.coverage(
    branch=True,
    include="journalmylife/*",
    omit=[
        "journalmylife/tests/*",
        "journalmylife/config.py",
        "journalmylife/tests/*",
        "journalmylife/*/__init__.py",
    ],
)

COV.start()

from journalmylife.journal import app, db
from journalmylife.database import models

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command("db", MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover("journalmylife/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def create_db():
    """Creates all the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops all the db tables."""
    db.drop_all()


if __name__ == '__main__':
    manager.run()