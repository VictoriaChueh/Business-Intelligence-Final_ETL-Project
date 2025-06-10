# 將 SQLite 中的資料輸出為 CSV
import sqlite3
import pandas as pd

conn = sqlite3.connect("mars_rover_photos.db")
df = pd.read_sql_query("SELECT * FROM photos_summary", conn)
df.to_csv("mars_photos_for_tableau.csv", index=False)
conn.close()