import sqlite3
from sqlite3 import IntegrityError

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
city TEXT NOT NULL
)
''')


def add_user(id: int, city: str):
    try:
        cursor.execute('DELETE FROM Users WHERE id = ?', (id,))
    except IntegrityError:
        pass
    cursor.execute('INSERT INTO Users (id, city) VALUES (?, ?)', (id, city))
    connection.commit()


def delete_user(id: int):
    cursor.execute('DELETE FROM Users WHERE id = ?', (id,))
    connection.commit()