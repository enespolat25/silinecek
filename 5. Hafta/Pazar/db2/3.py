import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

sql_command = """UPDATE book SET author = 'Author' WHERE book_id = 4;"""

cursor.execute(sql_command)
connection.commit()

connection.close()