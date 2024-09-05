import sqlite3

db_name = "blog.db"
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def get_categories():
    open()
    cursor.execute("SELECT * FROM category")
    res = cursor.fetchall()
    close()
    return res

def get_pos():
    open()
    cursor.execute("SELECT * FROM post")
    res = cursor.fetchall()
    close()
    return res

def get_PosByCategory(category_id):
    open()
    cursor.execute("SELECT * FROM post WHERE category_id = ?", [category_id])
    res = cursor.fetchall()
    close()
    return res