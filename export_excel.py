import sqlite3
import pandas as pd


def export_to_excel():
    conn = sqlite3.connect("emails.db")

    query = "SELECT sender, subject, time FROM emails"
    df = pd.read_sql_query(query, conn)

    df.to_excel("emails.xlsx", index=False)

    conn.close()