import sqlite3
connection = sqlite3.connect('bd.db')
connection.close()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')
connection.commit()
connection.close()
