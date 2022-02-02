import io
import os
import sqlite3
import sys

import pytest
from src.shop_cli import *

from src import conf

""" Will check to flow of the PhoneShop by sending input mocks to the CLI"""


def mock_input(val):
    ins = io.StringIO(val)
    sys.stdin = ins


@pytest.fixture()
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


def test_phone_addition_CLI(db):
    """Testing the CLI to add new phone"""
    try:
        mock_input('\n'.join(["0", "iphone", "x", "1800", "1", "01565766", "20-1-2024"]))
        mock_input('\n'.join(["0", "xiaomi", "10T", "1200", "3", "11565766", "20-11-2022"]))
        iphone = db_utils.get_phone_by_model(db, "x")
        xiaomi = db_utils.get_phone_by_model(db, "10T")
        assert iphone[0] == "iphone" and iphone[4] == "01565766"
        assert xiaomi[0] == "xiaomi" and xiaomi[4] == "11565766"
        cli(db)
    except EOFError:
        return

def test_update_quantity_CLI(db):
    """Testing the CLI to upate phone quantity"""
    try:
        mock_input('\n'.join(["1", "x","3"]))
        mock_input('\n'.join(["1","10T", "0", "3"]))
        iphone = db_utils.get_phone_by_model(db, "x")
        xiaomi = db_utils.get_phone_by_model(db, "10T")
        assert iphone[0] == "iphone" and iphone[3] == "1"
        assert xiaomi[0] == "xiaomi" and xiaomi[3] == "0"
        cli(db)
    except EOFError:
        return
