import sqlite3

DB_NAME = "database.db"


def get_db():
    connection = sqlite3.connect(DB_NAME)
    return connection


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
