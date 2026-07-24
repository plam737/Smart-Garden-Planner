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

def update_garden(garden_id, username, garden_type, shape, length, width, diameter):
    conn = sqlite3.conenct("users.db")
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE gardens SET garden_type = ?, shape = ?, length = ?, width = ?, diameter = ? WHERE garden_id = ? AND username = ?""", 
        (garden_type, shape, length, width, diameter, garden_id, username)
    )
    conn.commit()
    conn.close()

def delete_garden(garden_id, username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM gardens WHERE garden_id = ? AND username = ?", (garden_id, username)
    )
    conn.commit()
    conn.close()