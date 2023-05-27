import sqlite3
connection = sqlite3.connect("books.db")

# used as an interface to execute all SQL commands
cursor = connection.cursor()

# delete (uncomment below statement if table needs to be recreated)
# cursor.execute("""DROP TABLE book;""")

#SQL commands could be defined using triple quoted string
sql_command = """
CREATE TABLE book (
book_id INTEGER PRIMARY KEY,
book_title VARCHAR(200),
author VARCHAR(100),
publication_year INTEGER);"""

#Execute command performs the actual SQL operation
cursor.execute(sql_command)

#Close connection at the end of every database use
connection.close() 