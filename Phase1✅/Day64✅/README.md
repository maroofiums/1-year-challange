# Day 64

Welcome to Day 64 of the 365 Days of Code Challenge!



---

## 🗂️ 1. **Tables**

A **table** is like a spreadsheet with rows and columns.

### 📌 Example Table: `Students`

| id | name   | age | course     |
| -- | ------ | --- | ---------- |
| 1  | Ayesha | 20  | Computer   |
| 2  | Maroof | 21  | Software   |
| 3  | Tanvir | 22  | Electrical |

**Basic Table Creation:**

```sql
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
```

---

## 🔍 2. **Queries (SELECT, INSERT, UPDATE, DELETE)**

### a. **SELECT** – Read data

```sql
SELECT * FROM Students;
SELECT name, age FROM Students WHERE age > 20;
```

### b. **INSERT** – Add data

```sql
INSERT INTO Students (id, name, age, course)
VALUES (4, 'Sara', 19, 'Mechanical');
```

### c. **UPDATE** – Modify data

```sql
UPDATE Students
SET age = 23
WHERE name = 'Tanvir';
```

### d. **DELETE** – Remove data

```sql
DELETE FROM Students WHERE id = 1;
```

---

## 🔗 3. **Joins**

Used to combine rows from two or more tables based on related columns.

### Example Tables:

#### `Students`

| id | name   |
| -- | ------ |
| 1  | Maroof |
| 2  | Tanvir |

#### `Courses`

| student\_id | course |
| ----------- | ------ |
| 1           | Django |
| 2           | React  |

---

### a. **INNER JOIN** – Matches only related rows

```sql
SELECT Students.name, Courses.course
FROM Students
INNER JOIN Courses ON Students.id = Courses.student_id;
```

### b. **LEFT JOIN** – All rows from left table, even if no match

```sql
SELECT Students.name, Courses.course
FROM Students
LEFT JOIN Courses ON Students.id = Courses.student_id;
```

### c. **RIGHT JOIN** – All rows from right table, even if no match

```sql
SELECT Students.name, Courses.course
FROM Students
RIGHT JOIN Courses ON Students.id = Courses.student_id;
```

### d. **FULL OUTER JOIN** – All rows from both tables

```sql
SELECT Students.name, Courses.course
FROM Students
FULL OUTER JOIN Courses ON Students.id = Courses.student_id;
```

---

## 🧠 Summary

| Concept   | Description                       | Example                         |
| --------- | --------------------------------- | ------------------------------- |
| **Table** | Structure to store data           | `CREATE TABLE`                  |
| **Query** | SQL command to manipulate data    | `SELECT`, `INSERT`, etc.        |
| **Join**  | Combine data from multiple tables | `INNER JOIN`, `LEFT JOIN`, etc. |

---

Would you like a small project or quiz to practice this?
