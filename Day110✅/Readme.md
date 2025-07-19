# Day110

---

### 🔸 Types of SQL JOINs

| JOIN Type      | Description                                                                            |
| -------------- | -------------------------------------------------------------------------------------- |
| **INNER JOIN** | Returns records with matching values in both tables.                                   |
| **LEFT JOIN**  | Returns all records from the left table, and the matched records from the right table. |
| **RIGHT JOIN** | Returns all records from the right table, and the matched records from the left table. |
| **FULL JOIN**  | Returns all records when there is a match in either left or right table.               |
| **CROSS JOIN** | Returns all combinations (Cartesian product) of rows from both tables.                 |
| **SELF JOIN**  | Joins a table with itself.                                                             |

---

### 📘 Syntax Examples

Assume we have two tables:

**Customers**

| customer\_id | name  |
| ------------ | ----- |
| 1            | Ali   |
| 2            | Sana  |
| 3            | Usman |

**Orders**

| order\_id | customer\_id | product |
| --------- | ------------ | ------- |
| 101       | 1            | Book    |
| 102       | 2            | Laptop  |
| 103       | 1            | Pen     |

---

### 🔹 INNER JOIN

```sql
SELECT Customers.name, Orders.product
FROM Customers
INNER JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

🔸 **Output:** Shows only matching `customer_id`s.

---

### 🔹 LEFT JOIN

```sql
SELECT Customers.name, Orders.product
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

🔸 **Output:** All customers, even those with no orders.

---

### 🔹 RIGHT JOIN

```sql
SELECT Customers.name, Orders.product
FROM Customers
RIGHT JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

🔸 **Output:** All orders, even if the customer is missing (rare case).

---

### 🔹 FULL JOIN

```sql
SELECT Customers.name, Orders.product
FROM Customers
FULL OUTER JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

🔸 **Output:** All customers and all orders (matched and unmatched).

---

### 🔹 CROSS JOIN

```sql
SELECT Customers.name, Orders.product
FROM Customers
CROSS JOIN Orders;
```

🔸 **Output:** Every customer paired with every product.

---

### 🔹 SELF JOIN

```sql
SELECT A.name AS Customer1, B.name AS Customer2
FROM Customers A, Customers B
WHERE A.customer_id <> B.customer_id;
```

🔸 **Output:** Each customer joined with every other customer.

