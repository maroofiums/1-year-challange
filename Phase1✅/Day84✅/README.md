# Day 84

---

## 📘 1. Tables

### ➤ What is a Table?

A **table** stores data in rows and columns, like a spreadsheet.

### Example: `Users` Table

| id | name    | email                                         |
| -- | ------- | --------------------------------------------- |
| 1  | Alice   | [alice@email.com](mailto:alice@email.com)     |
| 2  | Bob     | [bob@email.com](mailto:bob@email.com)         |
| 3  | Charlie | [charlie@email.com](mailto:charlie@email.com) |

### SQL to Create It:

```sql
CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

### Insert Data:

```sql
INSERT INTO Users (id, name, email) VALUES (1, 'Alice', 'alice@email.com');
```

---

## 🔍 2. Queries

### ➤ SELECT: Fetch data

```sql
-- Get all users
SELECT * FROM Users;

-- Get only names
SELECT name FROM Users;

-- Get user with id = 2
SELECT * FROM Users WHERE id = 2;
```

### ➤ UPDATE: Modify data

```sql
UPDATE Users SET email = 'bob@new.com' WHERE name = 'Bob';
```

### ➤ DELETE: Remove data

```sql
DELETE FROM Users WHERE id = 3;
```

---

## 🔗 3. Joins

Joins combine data from **multiple tables** based on related columns.

### Example: Add an `Orders` Table

| id | user\_id | item     |
| -- | -------- | -------- |
| 1  | 1        | Laptop   |
| 2  | 1        | Keyboard |
| 3  | 2        | Mouse    |

```sql
CREATE TABLE Orders (
    id INT PRIMARY KEY,
    user_id INT,
    item VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
```

---

### 🔄 INNER JOIN: Matching records in both tables

```sql
SELECT Users.name, Orders.item
FROM Users
INNER JOIN Orders ON Users.id = Orders.user_id;
```

📌 **Result:**

| name  | item     |
| ----- | -------- |
| Alice | Laptop   |
| Alice | Keyboard |
| Bob   | Mouse    |

---

### 🧩 LEFT JOIN: All from left table + matches from right

```sql
SELECT Users.name, Orders.item
FROM Users
LEFT JOIN Orders ON Users.id = Orders.user_id;
```

📌 Includes users even if they haven’t placed an order.

---

### 🔎 Useful SQL Keywords:

* `WHERE` – filter records
* `ORDER BY` – sort results
* `GROUP BY` – group rows (use with aggregates like COUNT, SUM)
* `COUNT()` – counts rows
* `LIMIT` – limits results

---

## 🛠️ Practice Query

```sql
-- How many orders per user?
SELECT Users.name, COUNT(Orders.id) AS total_orders
FROM Users
LEFT JOIN Orders ON Users.id = Orders.user_id
GROUP BY Users.name;
```

