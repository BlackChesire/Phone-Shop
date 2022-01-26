#!/usr/bin/python
import sqlite3
import sys
import src.db_util as db_utils
import src.conf as conf
from Phone import *
import Sale

cmd_dict = {
    "0": "Add a new phone",
    "1": "Update Phone quantity",
    "2": "Add new sale",
    "4": "Get report of all phones in stock",
    "5": "Get report of total amount of sales between dates",
    "6": "EXIT"
}

def cli(connection):

    print("------------> Welcome to the phone store CLI <------------")
    for i in cmd_dict:
        print(f'press {i} in order to {cmd_dict[i]}')
    selection = input("Enter selection: ")
    while selection not in cmd_dict.keys():
        print("wrong selection please try again")
        cli(connection)
    cmd_management(selection)


def cmd_management(selection):
    print(f"You chose: {cmd_dict[selection]}")
    match selection:
        case 1:  # add new phone
            # getting user input 1 by 1 in order to avoid wrong input
            manufacturer = input("please enter manufacturer: ")
            model = input("please enter model: ")
            price = input("please enter price: ")
            quantity = input("please enter quantity: ")
            imei = input("please enter IMEI: ")
            warranty = input("please enter warranty end date: ")
            new_phone = Phone(manufacturer, model, price, quantity, imei, warranty)
            db_utils.add_new_phone(connection, new_phone)
            return
        case 2:  # update phone quantity
            imei = input("please enter the phone's IMEI")
            new_quantity = input("enter new quantity")
            db_utils.update_phone_quantity(connection,imei,new_quantity)

            return
        case 3:  # add new sale
            return
        case 4:  # phone stock report
            db_utils.get_phone_stock_report(connection)
            return
        case 5:  # total amount of sales between dates
            start_date = input("Enter start date:")
            end_date = input("Enter end date:")
            db_utils.sales_report_by_date(connection, start_date, end_date)
            return
        case 6:  # EXIT
            exit()


if __name__ == '__main__':
    connection = None
    try:
        connection = db_utils.create_db()
        db_utils.load_raw_data(connection)
        cli(connection)
        # db_utils.select_all_by_table(connection, conf.PHONE_TABLE)
        # db_utils.select_all_by_table(connection, conf.SALE_TABLE)
        # db_utils.get_phone_stock_report(connection)
    except sqlite3.Error as e:
        print(f"Error {e.args[0]}")
        sys.exit(1)
    finally:
        if connection:
            connection.close()
