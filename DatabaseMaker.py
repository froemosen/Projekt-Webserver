import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE Covid (Land TEXT, Smittede INTEGER, Doede INTEGER, Date TEXT)')
print("Table created successfully")
conn.close()
