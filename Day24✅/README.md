# Day 24

Welcome to Day 24 of the 365 Days of Code Challenge!
SQLite3 is a lightweight, built-in SQL database engine that's integrated into Python through the `sqlite3` module. It allows you to create and manage databases directly from Python scripts without requiring a separate server.

Here’s a basic guide to using SQLite3 in Python:

---

### 🔹 1. **Import the Module**

```python
import sqlite3
```

---

### 🔹 2. **Connect to a Database**

If the database file doesn’t exist, it will be created automatically.

```python
conn = sqlite3.connect('mydatabase.db')
```

---

### 🔹 3. **Create a Cursor**

A cursor allows you to execute SQL commands.

```python
cursor = conn.cursor()
```

---

### 🔹 4. **Create a Table**

```python
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
```

---

### 🔹 5. **Insert Data**

```python
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
```

Use `?` to prevent SQL injection.

---

### 🔹 6. **Fetch Data**

```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

Or fetch one record:

```python
row = cursor.fetchone()
```

---

### 🔹 7. **Update Data**

```python
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Alicia", 1))
```

---

### 🔹 8. **Delete Data**

```python
cursor.execute("DELETE FROM users WHERE id = ?", (1,))
```

---

### 🔹 9. **Commit Changes & Close Connection**

```python
conn.commit()
conn.close()
```

---

### ✅ Sample Full Program

```python
import sqlite3

# Connect
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
''')

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Maroof", "maroof@example.com"))

# Fetch data
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Commit & close
conn.commit()
conn.close()
```

---

If you'd like, I can guide you through a **mini project** using SQLite3, like a TODO app or blog database. Just let me know!
