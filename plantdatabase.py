import sqlite3

def add_plant(garden_id, username, plant_name, planting_date, status, notes):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO plants (garden_id, username, plant_name, planting_date, status, notes) VALUES (?, ?, ?, ?, ?, ?)
        """, (garden_id, username, plant_name, planting_date, status, notes))
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

def log_watering(planted_id, username, watering_date):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO watering_log (planted_id, username, watering_date) VALUES (?, ?, ?)
        """, (planted_id, username, watering_date)
    )
    conn.commit()
    conn.close()

def log_harvest(planted_id, username, harvest_date, notes):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO harvest_log (planted_id, username, harvest_date, notes) VALUES (?, ?, ?, ?)
        """, (planted_id, username, harvest_date, notes)
    )
    conn.commit()
    conn.close()

def get_watering_log(planted_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM watering_log WHERE planted_id = ?
        """, (planted_id,)
    )
    waterings = cursor.fetchall()
    conn.close()
    return waterings


def delete_old_watering_logs(planted_id, cutoff_date):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM watering_log WHERE planted_id = ? AND watering_date < ?
        """, (planted_id, cutoff_date)
    )
    conn.commit()
    conn.close()

def update_plant_status(planted_id, username, status):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE plants SET status = ? WHERE planted_id = ? AND username = ?
        """, (status, planted_id, username)
    )
    conn.commit()
    conn.close()

def get_active_plants(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM plants WHERE username = ? AND status != 'ready for removal'    
        """, (username,)
    )
    plants_selected = cursor.fetchall()
    conn.close()
    return plants_selected

def get_harvest_log(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM harvest_log WHERE username = ?
        """, (username,)
    )
    harvest_logs = cursor.fetchall()
    conn.close()
    return harvest_logs

def delete_plant_logs(planted_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM watering_log WHERE planted_id = ?
        """, (planted_id,)
    )
    cursor.execute("""
        DELETE FROM harvest_log WHERE planted_id = ? 
        """, (planted_id,)
    )
    conn.commit()
    conn.close()