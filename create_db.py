import sqlite3

conn = sqlite3.connect('users_db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users_tb(
                                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT,
                                    user_last_name TEXT,
                                    user_role TEXT,
                                    user_password TEXT)""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS users_right(
                                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT,
                                    user_lastname TEXT,
                                    user_role TEXT,
                                    user_password TEXT)""")
conn.commit()
conn.close()
