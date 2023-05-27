import sqlite3


#
# Establishing connection
#

# open a SQLite connection
# a database file called data.db will be created,
# if it does not exist
connection = sqlite3.connect('data.db')

# create a database cursor
cur = connection.cursor()

#
# Creating the table
#

# create the database table if it doesn't exist
table_schema = """
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);
"""
cur.execute(table_schema)

#
# Querying the database
#

# query the database for ALL data in the notes table
cur.execute('SELECT * FROM notes;')

# print the result
result = cur.fetchall()
print(result)

#
# Cleaning up
#

# close the cursor
cur.close()

# close the connection
connection.close()