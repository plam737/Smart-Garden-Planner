import sqlite3

def add_plant(garden_id, username, plant_name, planting_date, notes):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO plants (garden_id, username, plant_name, planting_date, notes) VALUES (?, ?, ?, ?, ?)
        """, (garden_id, username, plant_name, planting_date, notes))
    conn.commit()
    conn.close()

def get_garden_plants(garden_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM plants WHERE garden_id = ?
    """, (garden_id,))
    plants = cursor.fetchall()
    conn.close()
    return plants

def delete_plant(planted_id, username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM plants WHERE planted_id = ? AND username = ?
    """, (planted_id, username))
    conn.commit()
    conn.close()