import os
import sqlite3
import pytest
from src.shop_cli import *

from src import conf

""" Will check to flow of the PhoneShop by sending input mocks to the CLI"""


@pytest.fixture
def db():
    """configure test DB """
    if os.path.isfile(conf.TEST_DB):
        print("Database exist, skip create")
        return sqlite3.connect(f'file:{conf.TEST_DB}?mode=rw', uri=True)
    else:
        conn = sqlite3.connect(conf.TEST_DB)
        for table in conf.TABLES.values():
            conn.cursor().execute(table)
        return conn


def test_run_cli(db):
    """running test flow with cli on the Test DB"""
    cli(db)
    # with mock.patch('builtins.input', return_value="yes"):
