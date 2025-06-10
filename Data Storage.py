#Data Storage

import sqlite3
import pandas as pd
import os

# 1. Read the cleaned data
input_path = os.path.expanduser("~/data/processed/mars_rover_photos_summary_cleaned.csv")
df_cleaned = pd.read_csv(input_path)

# 2. Establish SQLite database connection (creates the database file if it doesn't exist)
conn = sqlite3.connect("mars_rover_photos.db")

# 3. Write data to the table: photos_summary
df_cleaned.to_sql("photos_summary", conn, if_exists="replace", index=False)

print("✅ Data successfully written to the 'photos_summary' table in 'mars_rover_photos.db'")

# 4. Query: Number of records for each rover
query = "SELECT rover, COUNT(*) as count FROM photos_summary GROUP BY rover"
result = pd.read_sql_query(query, conn)

print("\n📊 Number of records per rover:")
print(result)

# 5. Close the connection
conn.close()