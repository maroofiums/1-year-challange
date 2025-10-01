# Day159

## **SQL Joins**



1. **INNER JOIN**

   * Returns rows that match in *both* tables.
   * Like saying: “only give me the overlap.”

   ```sql
   SELECT u.id, u.name, o.order_id
   FROM users u
   INNER JOIN orders o ON u.id = o.user_id;
   ```

   👉 Only users who *actually placed orders* show up.

2. **LEFT JOIN** (aka LEFT OUTER JOIN)

   * Returns *all rows* from the left table, and matching rows from the right.
   * If no match, you’ll get NULLs.

   ```sql
   SELECT u.id, u.name, o.order_id
   FROM users u
   LEFT JOIN orders o ON u.id = o.user_id;
   ```

   👉 All users show up, even those who never ordered (their `order_id` will just be NULL).

3. **RIGHT JOIN** (mirror of LEFT JOIN, but less common)

   * Returns all rows from the right table, and matches from the left.
   * Usually, you can just flip your query with a LEFT JOIN instead of using RIGHT JOIN.

4. **FULL OUTER JOIN**

   * Returns all rows from both sides. If there’s no match, fills with NULLs.
   * Not supported in MySQL (but you can hack it with a `UNION`).

   ```sql
   SELECT u.id, u.name, o.order_id
   FROM users u
   FULL OUTER JOIN orders o ON u.id = o.user_id;
   ```

5. **CROSS JOIN**

   * Cartesian product: every row from table A paired with every row from table B.
   * Almost never what you want unless you’re intentionally generating combos.

---

### **SQL Relationships**

This is the **why** behind joins. In relational databases, tables are linked by **keys**:

* **Primary Key (PK)** → unique identifier for a row (`user_id` in `users`).
* **Foreign Key (FK)** → column that references another table’s PK (`user_id` in `orders`).

Common relationship types:

1. **One-to-One**

   * Each row in Table A has at most one matching row in Table B.
   * Rare, usually when splitting off optional or sensitive data.

2. **One-to-Many** (most common)

   * One row in Table A maps to many rows in Table B.
   * Example: one `user` → many `orders`.

3. **Many-to-Many**

   * Each row in A can map to many in B, and vice versa.
   * Needs a junction table.
   * Example: `students` ↔ `courses` with a `student_courses` table linking them.

---

🔥 Bottom line:

* **Joins** = how you *query* related data.
* **Relationships** = how you *design* related data.
