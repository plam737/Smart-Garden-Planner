import sqlite3
import bcrypt

def initialize_db():
    # Initialize the database connection and create tables if they don't exist
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            name TEXT,
            city TEXT,
            hard_zone TEXT,
            units TEXT       
        )
    ''')
    conn.commit()
    conn.close()

def create_new_user(username, password, name, city, hard_zone, units):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''
        INSERT INTO users (username, password, name, city, hard_zone, units)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (username, hashed_pwd, name, city, hard_zone, units))
    conn.commit()
    conn.close()

def find_returning_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if user is None:
        return "User not found"
    pwd_check = bcrypt.checkpw(password.encode('utf-8'), user[1])
    if pwd_check:
        return user
    else:
        return "Password incorrect"

def get_user_by_username(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    if user is None:
        return "User not found"
    return user

