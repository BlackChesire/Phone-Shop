import src.db_util as db_utils
from src.Phone import *
from src.Sale import *

connection = db_utils.create_db()


def test_add_new_phone():
    xiaomi = Phone("xiaomi", "mi10", 1500, 3, "0123456", 20 - 9 - 22)
    iphone = Phone("iphone", "x", 1800, 1, "01565766", 20 - 1 - 24)
    mini = Phone("iphone", "12 mini", 2000, 1, "01256856", 22 - 7 - 21)
    samsung = Phone("samsung", "s10", 1500, 4, "0123456", 11 - 6 - 25)
    db_utils.add_new_phone(connection, iphone)
    db_utils.add_new_phone(connection, mini)
    db_utils.add_new_phone(connection, samsung)
    db_utils.add_new_phone(connection, xiaomi)


def test_update_phone_quantity():
    db_utils.update_phone_quantity(connection, "mi10", 1)
    db_utils.update_phone_quantity(connection, "x", 3)
    db_utils.update_phone_quantity(connection, "12 mini", 0)
    db_utils.update_phone_quantity(connection, "s10", 5)
    db_utils.update_phone_quantity(connection, "mi10", 1)


def test_add_new_sale():
    pass


def test_sales_by_date():
    pass


def test_get_phone_stock_report():
    pass


def test_sales_report_by_date():
    pass


def test_get_price_by_model():
    pass
