#!/usr/bin/python

import yaml
import sqlite3
import os.path
import src.conf as conf


def create_db():
    if os.path.isfile(conf.DB_NAME):
        print("Database exist, skip create")
        return sqlite3.connect(f'file:{conf.DB_NAME}?mode=rw', uri=True)
    else:
        conn = sqlite3.connect(conf.DB_NAME)
        for table in conf.TABLES.values():
            conn.cursor().execute(table)
        return conn


def load_raw_data(conn):
    with open(r'db/raw_data.yaml') as file:
        records = yaml.load(file, Loader=yaml.FullLoader)
        for key in records.keys():
            for item in records[key]:
                conn.cursor().execute(
                    f"INSERT INTO {key} VALUES({records[key][item]})"
                )
                conn.commit()


def select_all_by_table(conn, table_name):
    print(f"\nAll data in table:{table_name}")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def add_new_phone(conn, phone):
    """ Adds new phone to the phones table"""
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO {conf.PHONE_TABLE} VALUES ('{phone.manufacturer}' ,'{phone.model}',{phone.price} ,{phone.quantity},{phone.IMEI} ,'{phone.warranty}') ")
    conn.commit()


def get_phone_by_model(conn, phone_model):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {conf.PHONE_TABLE} WHERE model = '{phone_model}'")
    phone = cur.fetchall()
    return phone[0]


def update_phone_quantity(conn, model, quantity):
    cur = conn.cursor()
    cur.execute(f"UPDATE {conf.PHONE_TABLE} SET quantity = {quantity} WHERE model = '{model}' ")
    conn.commit()


def add_new_sale(conn, sale):
    discount = None
    cur = conn.cursor()
    if sale.discount_made == 1:
        discount = 0
    cur.execute(
        f"INSERT INTO {conf.SALE_TABLE} VALUES ('{sale.manufacturer}' ,'{sale.model}',{sale.total_sale} ,'{sale.amount_sold}','{sale.date}',{discount}) ")
    # Update sold phone quantity stock
    cur.execute(f"UPDATE {conf.PHONE_TABLE} SET quantity = quantity - {sale.amount_sold} WHERE model = '{sale.model}'")
    conn.commit()


def get_sales_by_date(conn, sale_date):
    cur = conn.cursor()
    cur.execut(f"SELECT * FROM {conf.SALE_TABLE} WHERE  date_of_purchase = {sale_date}")
    sales = cur.fetchall()
    return sales


# Report handling
def get_phone_stock_report(conn):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {conf.PHONE_TABLE} WHERE quantity > 0")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def sales_report_by_date(conn, start_date, end_date):
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM {conf.SALE_TABLE} WHERE '{end_date}' > date_of_purchase AND '{start_date}' > date_of_purchase")
    rows = cur.fetchall()
    print(f"Total sales between {start_date} and {end_date} is : {len(rows)}")


def get_price_by_model(conn, phone_model, manu):
    cur = conn.cursor()
    cur.execute(f"SELECT price FROM {conf.PHONE_TABLE} WHERE model = '{phone_model}' AND manufacturer = '{manu}'")
    price = cur.fetchone()
    return price[0]
