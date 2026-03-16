import sqlite3
import pandas as pd

conn = sqlite3.connect("emails.db")

# Filter example
query = """
SELECT sender, subject, time, folder
FROM emails
WHERE sender NOT LIKE '%noreply%'
"""

df = pd.read_sql_query(query, conn)

df.to_csv("filtered_emails.csv", index=False)

print("Filtered CSV Exported")