import sqlite3
import csv


def export_to_csv():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("SELECT sender, subject, time FROM emails")
    rows = cursor.fetchall()

    with open("emails.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Sender", "Subject", "Time"])
        writer.writerows(rows)

    conn.close()