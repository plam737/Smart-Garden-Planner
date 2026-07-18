import sqlite3

def create_new_garden(username, garden_type, shape, length, width, diameter):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO gardens VALUES (?, ?, ?, ?, ?, ?)
    """, (username, garden_type, shape, length, width, diameter))
    conn.commit()
    conn.close()

def get_new_garden(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        "SELECT * FROM gardens WHERE username = ?", ((username,))  
    """)
    gardens = cursor.fetchall()
    conn.close()
    return gardens