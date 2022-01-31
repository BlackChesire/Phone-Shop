import sqlite3
import sys
import pytest
import src.db_util as db_utils
# import src.conf as conf
from src.Phone import *
from src.Sale import *

connection = db_utils.create_db()
db_utils.load_raw_data(connection)


@pytest.fixture
def test_add_new_phone():
    xiaomi = Phone("xiaomi", "mi10", 1500, 3, "0123456", 20 - 9 - 22)
    iphone = Phone("iphone", "x", 1800, 1, "01565766", 20 - 1 - 24)
    mini = Phone("iphone", "12 mini", 2000, 1, "01256856", 22 - 7 - 21)
    db_utils.add_new_phone(connection, iphone)
    db_utils.add_new_phone(connection, xiaomi)
    db_utils.add_new_phone(connection, mini)
    mi10 = db_utils.get_phone_by_model(connection, "mi10")
    iphone_x = db_utils.get_phone_by_model(connection, "x")
    mini_12 = db_utils.get_phone_by_model(connection, "12 mini")


@pytest.fixture
def test_update_phone_quantity():
    db_utils.update_phone_quantity(connection, "mi10", 1)
    db_utils.update_phone_quantity(connection, "x", 3)
    db_utils.update_phone_quantity(connection, "12 mini", 0)
    mi10 = db_utils.get_phone_by_model(connection, "mi10")
    iphone_x = db_utils.get_phone_by_model(connection, "x")
    mini_12 = db_utils.get_phone_by_model(connection, "12 mini")


@pytest.fixture
def test_add_new_sale():
    xiaomi_sale = Sale("xiaomi", "mi10", "22 - 1 - 21", 1, 2400, 0.16)
    iphone_sale = Sale("iphone", "x", "20 - 3 - 22", 1, 2000, 0)
    db_utils.get_sales_by_date(connection, "22 - 1 - 21")
    pass


@pytest.fixture
def test_sales_by_date():
    pass


@pytest.fixture
def test_get_phone_stock_report():
    db_utils.get_phone_stock_report(connection)
    pass


@pytest.fixture
def test_sales_report_by_date():
    pass


@pytest.fixture
def test_get_price_by_model():
    iphone_price = db_utils.get_price_by_model(connection, "x", "iphone")
    samsung_price = db_utils.get_price_by_model(connection, "s10", "samsung")
    pass
