import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM book") 

print("Book list:")               
results = cursor.fetchall()
for row in results:
    print(row)

connection.close()