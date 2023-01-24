from init_db import get_db


def insert_user(name):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(name) VALUES (?)"
    cursor.execute(statement, [name])
    db.commit()
    return True


def update_user(id, name):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE users SET name = ? WHERE id = ?"
    cursor.execute(statement, [name, id])
    db.commit()
    return True


def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM users WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name FROM users WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name FROM users"
    cursor.execute(query)
    return cursor.fetchall()
