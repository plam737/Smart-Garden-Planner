import sqlite3
import bcrypt

def initialize_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            name TEXT,
            city TEXT,
            state TEXT,
            units TEXT,
            plant_variety TEXT,
            frequency TEXT,
            hard_zone TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gardens (
            garden_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            garden_type TEXT,
            shape TEXT, 
            length REAL, 
            width REAL,
            diameter REAL
        )
    """)
    conn.commit()
    conn.close()

def create_new_user(username, password, name, city, state, units, plant_variety, frequency, hard_zone):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute("""
    INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (username, hashed_pwd, name, city, state, units, plant_variety, frequency, hard_zone))
    conn.commit()
    conn.close()

def find_returning_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user is None:
        return "User not found"
    pwd_check = bcrypt.checkpw(password.encode('utf-8'), user[1])
    if pwd_check: 
        return user
    else:
        return "Password incorrect"
    
def update_name(username, name):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ? WHERE username = ?", (name, username))
    conn.commit()
    conn.close()

def update_units(username, units):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET units = ? WHERE username = ?", (units, username))
    conn.commit()
    conn.close()

def update_plant_variety(username, plant_variety):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET plant_variety = ? WHERE username = ?", (plant_variety, username))
    conn.commit()
    conn.close()

def update_frequency(username, frequency):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET frequency = ? WHERE username = ?", (frequency, username))
    conn.commit()
    conn.close()

def update_location(username, city, state, hard_zone, units):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET city = ?, state = ?, hard_zone = ?, units = ? WHERE username = ?", (city, state, hard_zone, units, username))
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user