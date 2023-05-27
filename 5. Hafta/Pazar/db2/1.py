import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

book_data = [ ("Automate the Boring Stuff with Python: Practical Programming for Total Beginners", "Al Sweigart", "2015"),
               ("Python for Everybody: Exploring Data in Python 3", "Dr. Charles Russell Severance, Sue Blumenberg, Elliott Hauser, Aimee Andrion", "2016"),
               ("Dive Into Python 3", "Mark Pilgrim", "2012"),
               ("Test Book", "Test Author", "2020"), ]

for row in book_data:
    format_str = """INSERT INTO book (book_id, book_title, author, publication_year)
    VALUES (NULL, "{name}", "{author}", "{pub_year}");"""

    sql_command = format_str.format(name=row[0], author=row[1], pub_year=row[2])
    cursor.execute(sql_command)

connection.commit()
connection.close()