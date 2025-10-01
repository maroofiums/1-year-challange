# **Day145**

## 🔗 Database Relationships

In relational databases, **relationships** define how tables are logically connected.

1. **One-to-One (1:1)**

   * One row in **Table A** relates to only one row in **Table B**.
   * Example: A `user` table and a `user_profile` table.

2. **One-to-Many (1\:N)**

   * One row in **Table A** can relate to many rows in **Table B**, but each row in **Table B** relates to only one row in **Table A**.
   * Example: A `customer` can have many `orders`.

3. **Many-to-Many (M\:N)**

   * Rows in **Table A** can relate to multiple rows in **Table B** and vice versa.
   * Implemented with a **junction table**.
   * Example: `students` and `courses` with a `student_courses` table.

---

## 🛠 SQL JOINs

JOINs allow you to query data across related tables.

### 1. **INNER JOIN**

* Returns rows where there’s a match in both tables.

```sql
SELECT c.customer_id, c.name, o.order_id
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
```

### 2. **LEFT JOIN (LEFT OUTER JOIN)**

* Returns all rows from the **left** table, plus matching rows from the right.
* If no match exists, `NULL` is returned for right table columns.

```sql
SELECT c.customer_id, c.name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
```

### 3. **RIGHT JOIN (RIGHT OUTER JOIN)**

* Opposite of `LEFT JOIN`.
* All rows from the **right** table + matches from the left.

### 4. **FULL OUTER JOIN**

* Returns all rows from both tables, with `NULL` for non-matching rows.

```sql
SELECT c.customer_id, c.name, o.order_id
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id;
```

### 5. **CROSS JOIN**

* Returns Cartesian product (all combinations).

```sql
SELECT a.name, b.product
FROM employees a
CROSS JOIN products b;
```

### 6. **SELF JOIN**

* A table joins with itself.

```sql
SELECT e1.employee_id, e1.name, e2.name AS manager
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

---

## 🔑 How JOINs Map to Relationships

* **1:1** → Usually `INNER JOIN` or `LEFT JOIN` (depending on required results).
* **1\:N** → Very common with `INNER JOIN` or `LEFT JOIN`.
* **M\:N** → Requires a junction table with two foreign keys, usually joined with two `INNER JOIN`s.

---
