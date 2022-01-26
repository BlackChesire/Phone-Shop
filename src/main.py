#!/usr/bin/python
import sqlite3
import sys
import src.db_util as db_utils
import src.conf as conf
import Phone
import Sale


def cli():
    cmd_dict = {
        "0": "Add a new phone",
        "1": "Update Phone quantity",
        "2": "Add new sale",
        "4": "Get report of all phones in stock",
        "5": "Get report of total amount of sales between dates",
        "6": "EXIT"
    }
    print("------------> Welcome to the phone store CLI <------------")
    for i in cmd_dict:
        print(f'press {i} in order to {cmd_dict[i]}')
    selection = input("Enter selection: ")
    cmd_management(selection)


def cmd_management(selection):
    match selection:
        case 1:  # add new phone
            return
        case 2:  # update phone quantity
            return
        case 3:  # add new sale
            return
        case 4:  # phone stock report
            return
        case 5:  # total amount of sales between dates
            return
        case 6:  # EXIT
            exit()


if __name__ == '__main__':
    connection = None
    try:
        connection = db_utils.create_db()
        db_utils.load_raw_data(connection)
        cli()
        # phone = Phone.Phone("apple", "iphone", 2400, 2, 123456, "20.1.22")
        # db_utils.add_new_phone(connection,phone)
        # db_utils.update_phone_quantity(connection,123456,3)
        # db_utils.select_all_by_table(connection, conf.PHONE_TABLE)
        # db_utils.select_all_by_table(connection, conf.SALE_TABLE)
        # db_utils.get_phone_stock_report(connection)
    except sqlite3.Error as e:
        print(f"Error {e.args[0]}")
        sys.exit(1)
    finally:
        if connection:
            connection.close()
