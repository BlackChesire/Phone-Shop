#!/usr/bin/python
import sqlite3
import sys
from src.shop_cli import *

if __name__ == '__main__':
    connection = None
    try:
        connection = db_utils.create_db()
        db_utils.load_raw_data(connection)
        cli(connection)
    except sqlite3.Error as e:
        print(f"Error {e.args[0]}")
    finally:
        if connection:
            connection.close()
            sys.exit(1)
