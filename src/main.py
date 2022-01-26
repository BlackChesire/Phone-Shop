#!/usr/bin/python
import sqlite3
import sys
import src.db_util as db_utils
import src.conf as conf
from Phone import *
from Sale import *

cmd_dict = {
    0: "Add a new phone",
    1: "Update phone quantity",
    2: "Add new sale",
    3: "Get report of all phones in stock",
    4: "Get report of total amount of sales between dates",
    5: "EXIT"
}


def cli(connection):
    print("------------> Welcome to the phone store CLI <------------")
    for i in cmd_dict:
        print(f'press {i} in order to {cmd_dict[i]}')
    selection = input("Enter selection: ")
    while int(selection) not in list(cmd_dict.keys()):
        print("wrong selection please try again")
        cli(connection)
    cmd_management(int(selection))
    cli(connection)


def cmd_management(selection):
    print(f"You chose: {cmd_dict[selection]}")
    match selection:
        case 0:  # add new phone
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
        case 1:  # update phone quantity
            model = input("please enter the phone's model")
            new_quantity = input("enter new quantity")
            db_utils.update_phone_quantity(connection, model, new_quantity)

            return
        case 2:  # add new sale
            manufacturer = input("Enter manufacturer: ")
            sold_model = input("Enter sold phone model: ")
            sale_date = input("Enter sale date model: ")
            amount = input(f"Enter amount of {sold_model} sold :")
            discount = input("Enter discount made for  (if none made enter 0):")
            if discount == 0.0:
                discount = 1
            acutal_phone_price = db_utils.get_price_by_model(connection, str(sold_model))
            sale = Sale(manufacturer, sold_model, sale_date, amount, acutal_phone_price * discount, discount)
            return
        case 3:
            # phone stock report
            db_utils.get_phone_stock_report(connection)
            return
        case 4:  # total amount of sales between dates
            start_date = input("Enter start date:")
            end_date = input("Enter end date:")
            db_utils.sales_report_by_date(connection, start_date, end_date)
            return
        case 5:  # EXIT
            exit()


if __name__ == '__main__':
    connection = None
    try:
        connection = db_utils.create_db()
        db_utils.load_raw_data(connection)
        cli(connection)
    except sqlite3.Error as e:
        print(f"Error {e.args[0]}")
        sys.exit(1)
    finally:
        if connection:
            connection.close()
