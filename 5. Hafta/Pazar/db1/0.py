# https://sqlitebrowser.org/dl/

import sqlite3


def create_connection(db_file):
    """ create a database connection to a SQLite Database"""
    try:
        with sqlite3.connect(db_file):
            print("Sqlite version :", sqlite3.version)
    except Exception as e:
        print(e)



create_connection("database.db")