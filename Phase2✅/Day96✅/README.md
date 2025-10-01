# Day 96


---

## 🔗 **What is a JOIN in SQL?**

A `JOIN` lets you combine data from two or more tables based on a **common column**, like a `user_id` or `product_id`.

---

### 📋 Example Tables:

#### 🧑‍💻 `users` table

| id | name   |
| -- | ------ |
| 1  | Ali    |
| 2  | Sana   |
| 3  | Maroof |

#### 📦 `orders` table

| id | user\_id | product    |
| -- | -------- | ---------- |
| 1  | 1        | Laptop     |
| 2  | 1        | Keyboard   |
| 3  | 2        | Headphones |

---

## 🔍 **Types of SQL JOINS with Code Examples**

---

### 1️⃣ **INNER JOIN**

> Returns only the rows that match in both tables.

```sql
SELECT users.name, orders.product
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

📌 **Result:**

```
Ali   | Laptop
Ali   | Keyboard
Sana  | Headphones
```

---

### 2️⃣ **LEFT JOIN (LEFT OUTER JOIN)**

> Returns all users, and matching orders if they exist.

```sql
SELECT users.name, orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

📌 **Result:**

```
Ali     | Laptop
Ali     | Keyboard
Sana    | Headphones
Maroof  | NULL
```

---

### 3️⃣ **RIGHT JOIN (RIGHT OUTER JOIN)**

> Returns all orders, and matching users if they exist.

```sql
SELECT users.name, orders.product
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;
```

📌 **Result:**

```
Ali   | Laptop
Ali   | Keyboard
Sana  | Headphones
```

*(No NULLs here because all orders have valid users)*

---

### 4️⃣ **FULL OUTER JOIN**

> Returns all users and all orders, even if they don’t match.

```sql
SELECT users.name, orders.product
FROM users
FULL OUTER JOIN orders ON users.id = orders.user_id;
```

📌 **Result:**

```
Ali     | Laptop
Ali     | Keyboard
Sana    | Headphones
Maroof  | NULL
NULL    | NULL
```

*(Shows users without orders + unmatched orders if any)*

---

### 5️⃣ **CROSS JOIN**

> Returns **every combination** of rows from both tables (Cartesian product).

```sql
SELECT users.name, orders.product
FROM users
CROSS JOIN orders;
```

📌 **Result:**
If 3 users × 3 orders = **9 rows total**
Every user matched with every product.

---

### 6️⃣ **SELF JOIN**

> A table joins with itself. Often used for parent-child relationships.

Example: Employee–Manager relationship.

```sql
SELECT A.name AS employee, B.name AS manager
FROM employees A
JOIN employees B ON A.manager_id = B.id;
```

📌 **Use Case:** Who works under whom?

---

## ✅ Quick Summary Table:

| JOIN Type         | Returns                            |
| ----------------- | ---------------------------------- |
| `INNER JOIN`      | Matching rows in both tables       |
| `LEFT JOIN`       | All left + matched right           |
| `RIGHT JOIN`      | All right + matched left           |
| `FULL OUTER JOIN` | All rows from both sides           |
| `CROSS JOIN`      | All combinations (left × right)    |
| `SELF JOIN`       | Join table with itself (hierarchy) |

---

## ✅ Practice Challenge

**Task:** Write a query to show users who have not placed any orders.

```sql
SELECT users.name
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.id IS NULL;
```


