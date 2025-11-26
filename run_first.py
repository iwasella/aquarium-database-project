import sqlite3

DB_NAME = "restaurant.db"

def run_sql_file(filename):
    with open(filename, "r") as f:
        return f.read()

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

print("🛠 Loading schema...")
cur.executescript(run_sql_file("schema.sql"))

print("🌱 Inserting seed data...")
cur.executescript(run_sql_file("seed_data.sql"))

conn.commit()
conn.close()

print("✅ Database successfully initialized!")
