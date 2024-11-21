import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Create tables for buyers and sellers
cursor.execute("""
CREATE TABLE IF NOT EXISTS buyers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    industry TEXT,
    revenue INTEGER,
    goals TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sellers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    industry TEXT,
    revenue INTEGER,
    goals TEXT
);
""")

# Insert sample data
buyers = [
    ('Tech Corp', 'Technology', 500000, 'Acquire innovative startups'),
    ('Health Inc', 'Healthcare', 1000000, 'Expand into new markets'),
]

sellers = [
    ('Innovate LLC', 'Technology', 400000, 'Exit and scale'),
    ('MediCare', 'Healthcare', 900000, 'Seek strategic partnerships'),
]

cursor.executemany("INSERT INTO buyers (name, industry, revenue, goals) VALUES (?, ?, ?, ?)", buyers)
cursor.executemany("INSERT INTO sellers (name, industry, revenue, goals) VALUES (?, ?, ?, ?)", sellers)

connection.commit()
connection.close()

print("Database setup complete!")
