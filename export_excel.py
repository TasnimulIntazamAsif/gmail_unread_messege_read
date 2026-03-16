import sqlite3
import pandas as pd

conn = sqlite3.connect("emails.db")

df = pd.read_sql_query("SELECT * FROM emails",conn)

df.to_excel("emails.xlsx",index=False)

print("Excel Exported")