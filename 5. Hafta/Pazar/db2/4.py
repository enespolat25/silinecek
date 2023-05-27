import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

sql_command = """DELETE FROM book WHERE book_id = 4;"""

cursor.execute(sql_command)
connection.commit()

connection.close()