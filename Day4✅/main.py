import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()
cursor.execute("CREATE TABLE Users (Id INTEGER,Email TEXT,Password TEXT)")
cursor.execute("INSERT INTO Users (Id,Email,Password) VALUES(1,'maroof2405208@gmail.com','maroof24052008')")
cursor.execute("INSERT INTO Users (Id,Email,Password) VALUES(2,'maroof2408@gmail.com','maroof24052008')")
cursor.execute("INSERT INTO Users (Id,Email,Password) VALUES(3,'maroof2208@gmail.com','maroof24052008')")
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for row in users:
    print(row[1])
conn.commit()
conn.close()