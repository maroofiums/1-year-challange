import sqlite3

# 1. Connect to SQLite DB (creates it if it doesn't exist)
conn = sqlite3.connect('join_example.db')
cursor = conn.cursor()

# 2. Create tables
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("DROP TABLE IF EXISTS users;")

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

# 3. Insert data
users = [(1, "Ali"), (2, "Sana"), (3, "Maroof")]
orders = [(1, 1, "Laptop"), (2, 1, "Keyboard"), (3, 2, "Headphones")]

cursor.executemany('INSERT INTO users VALUES (?, ?)', users)
cursor.executemany('INSERT INTO orders VALUES (?, ?, ?)', orders)
conn.commit()

# 4. INNER JOIN
print("\n📌 INNER JOIN:")
cursor.execute('''
SELECT users.name, orders.product
FROM users
INNER JOIN orders ON users.id = orders.user_id
''')
for row in cursor.fetchall():
    print(row)

# 5. LEFT JOIN
print("\n📌 LEFT JOIN:")
cursor.execute('''
SELECT users.name, orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id
''')
for row in cursor.fetchall():
    print(row)

# 6. Simulate RIGHT JOIN using LEFT JOIN + table switch
print("\n📌 RIGHT JOIN (Simulated):")
cursor.execute('''
SELECT users.name, orders.product
FROM orders
LEFT JOIN users ON orders.user_id = users.id
''')
for row in cursor.fetchall():
    print(row)

# 7. Simulate FULL OUTER JOIN using UNION
print("\n📌 FULL OUTER JOIN (Simulated):")
cursor.execute('''
SELECT users.name, orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id
UNION
SELECT users.name, orders.product
FROM orders
LEFT JOIN users ON orders.user_id = users.id
''')
for row in cursor.fetchall():
    print(row)

# 8. CROSS JOIN
print("\n📌 CROSS JOIN:")
cursor.execute('''
SELECT users.name, orders.product
FROM users
CROSS JOIN orders
''')
for row in cursor.fetchall():
    print(row)

# 9. SELF JOIN (if employee table)
print("\n📌 SELF JOIN Example:")
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    manager_id INTEGER
)
''')
employees = [
    (1, 'Ali', None),
    (2, 'Sana', 1),
    (3, 'Maroof', 1),
    (4, 'Ahmed', 2)
]
cursor.executemany('INSERT INTO employees VALUES (?, ?, ?)', employees)

cursor.execute('''
SELECT e1.name AS Employee, e2.name AS Manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id
''')
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
