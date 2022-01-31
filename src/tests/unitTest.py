import io
import os
import sys

from src.Phone import *
from src.Sale import *
import src.db_util as db_utils
import sqlite3
import src.conf as conf
import pytest
import yaml


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


def test_add_new_phone(db):
    xiaomi = Phone("xiaomi", "mi10", 1500, 3, "0123456", "20-9-2022")
    iphone = Phone("iphone", "x", 1800, 1, "01565766", "20-1-2024")
    mini = Phone("iphone", "12 mini", 2000, 1, "01256856", "22-7-2021")
    db_utils.add_new_phone(db, iphone)
    db_utils.add_new_phone(db, xiaomi)
    db_utils.add_new_phone(db, mini)
    mi10 = db_utils.get_phone_by_model(db, "mi10")
    mi10_mock = Phone(mi10[0], mi10[1], mi10[2], mi10[3], mi10[4], mi10[5])
    iphone_x = db_utils.get_phone_by_model(db, "x")
    iphone_mock = Phone(iphone_x[0], iphone_x[1], iphone_x[2], iphone_x[3], iphone_x[4], iphone_x[5])
    mini_12 = db_utils.get_phone_by_model(db, "12 mini")
    min_12_mock = Phone(mini_12[0], mini_12[1], mini_12[2], mini_12[3], mini_12[4], mini_12[5])
    assert xiaomi == mi10_mock
    assert iphone == iphone_mock
    assert min_12_mock == mini


def test_update_phone_quantity(db):
    db_utils.update_phone_quantity(db, "mi10", 1)
    db_utils.update_phone_quantity(db, "x", 3)
    db_utils.update_phone_quantity(db, "12 mini", 0)
    mi10 = db_utils.get_phone_by_model(db, "mi10")
    assert mi10[3] == 1
    iphone_x = db_utils.get_phone_by_model(db, "x")
    assert iphone_x[3] == 3
    mini_12 = db_utils.get_phone_by_model(db, "12 mini")
    assert mini_12[3] == 0


def test_add_new_sale(db):
    xiaomi_sale = Sale("xiaomi", "mi10", "22 - 1 - 21", 1, 2400, 0.16)
    iphone_sale = Sale("iphone", "x", "20 - 3 - 22", 1, 2000, 0)
    db_utils.add_new_sale(db, xiaomi_sale)
    db_utils.add_new_sale(db, iphone_sale)
    xiaomi_mock = db_utils.get_sale_by_date(db, "22 - 1 - 21")
    mock_xiaomi_sale = Sale(xiaomi_mock[0], xiaomi_mock[1], xiaomi_mock[4], xiaomi_mock[3], xiaomi_mock[2],
                            xiaomi_mock[5])
    iphone_mock = db_utils.get_sale_by_date(db, "20 - 3 - 22")
    mock_iphone_sale = Sale(iphone_mock[0], iphone_mock[1], iphone_mock[4], iphone_mock[3], iphone_mock[2],
                            iphone_mock[5])
    assert xiaomi_sale == mock_xiaomi_sale
    assert iphone_sale == mock_iphone_sale


def test_sales_by_date(db):
    pass


def test_get_phone_stock_report(db):
    db_utils.get_phone_stock_report(db)
    pass


def test_sales_report_by_date():
    pass


def test_get_price_by_model():
    iphone_price = db_utils.get_price_by_model(db, "x", "iphone")
    samsung_price = db_utils.get_price_by_model(db, "s10", "samsung")
    pass
