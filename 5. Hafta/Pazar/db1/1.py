# https://sqlitebrowser.org/dl/

import sqlite3

# open a SQLite connection
# a database file called data.db will be created,
# if it does not exist
connection = sqlite3.connect('data.db')

# close the connection
connection.close()