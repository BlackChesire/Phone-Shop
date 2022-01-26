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
    pass


def update_phone_quantity(conn, IMEI):
    pass


def add_new_sale(conn, phone, date):
    pass


def get_phone_stock_report(conn, phone, date):
    pass


def sales_report_by_date(conn, start_date, end_date):
    pass
