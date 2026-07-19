import sqlite3

def create_new_garden(username, garden_type, shape, length, width, diameter):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO gardens (username, garden_type, shape, length, width, diameter) VALUES (?, ?, ?, ?, ?, ?)
        """, (username, garden_type, shape, length, width, diameter))
    conn.commit()
    conn.close()

def get_user_gardens(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM gardens WHERE username = ?", ((username,))
    )
    gardens = cursor.fetchall()
    conn.close()
    return gardens