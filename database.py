import sqlite3

DB_NAME = "emails.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            subject TEXT,
            time TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_email(sender, subject, time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO emails (sender, subject, time)
        VALUES (?, ?, ?)
    """, (sender, subject, time))

    conn.commit()
    conn.close()