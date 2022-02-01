#!/usr/bin/python
from src.Phone import *
from src.Sale import *
import src.db_util as db_utils
cmd_dict = {
    # keys and commands for cli integration
    0: "Add a new phone",
    1: "Update phone quantity",
    2: "Add new sale",
    3: "Get report of all phones in stock",
    4: "Get report of total amount of sales between dates",
    5: "EXIT"
}


def cli(connection_string):
    """Command line interface - needs a connection string to the sqlite DB"""
    print("------------> Welcome to the phone store CLI <------------")
    for i in cmd_dict:
        print(f'press {i} in order to {cmd_dict[i]}')
    selection = input("Enter selection: ")
    while int(selection) not in list(cmd_dict.keys()):
        print("wrong selection please try again")
        cli(connection_string)
    cmd_management(int(selection), connection_string)
    cli(connection_string)


def cmd_management(selection, connection):
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
            actual_phone_price = db_utils.get_price_by_model(connection, str(sold_model), manufacturer)
            sale = Sale(manufacturer, sold_model, sale_date, amount, actual_phone_price * discount, discount)
            db_utils.add_new_sale(connection, sale)
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
            connection.close()
            exit()
