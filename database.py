import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS emails(
id INTEGER PRIMARY KEY AUTOINCREMENT,
sender TEXT,
subject TEXT,
time TEXT,
folder TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")