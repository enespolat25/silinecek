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
# Querying the database
#

# query the database for ALL data in the notes table
cur.execute('SELECT * FROM notes;')

# print the result
print('\nNotes:')
for row in cur.fetchall():
    display_name = row[1]
    display_desc = row[2]

    print(f'Not adi: {display_name}\nNot tanimi: {display_desc}\n')

# close the cursor
cur.close()

# close the connection
connection.close()