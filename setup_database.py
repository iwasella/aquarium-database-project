import sqlite3


DB_NAME = "restaurant.db"
SCHEMA_FILE = "schema.sql"

def initialize_db():
    print("📦 Connecting to database…")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("📄 Loading schema.sql…")
    with open(SCHEMA_FILE, "r") as f:
        schema = f.read()

    print("🛠 Creating tables (if not exist)…")
    cursor.executescript(schema)

    conn.commit()
    conn.close()
    print("✅ Database setup complete!")
    print(f"📁 Created / updated database file: {DB_NAME}")

if __name__ == "__main__":
    initialize_db()

