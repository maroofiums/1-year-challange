# Day 291

# PostgreSQL CRUD Operations – Company Database

This project demonstrates **basic SQL operations** using **PostgreSQL (psql CLI)**.  
It covers database creation, table setup, and complete **CRUD (Create, Read, Update, Delete)** operations using a `.sql` file.

---

## 📌 Features

- Create a PostgreSQL database
- Create a table with proper schema
- Insert multiple records
- Read data using SELECT queries
- Update existing records
- Delete specific records
- Execute SQL script using Command Line (psql)

---

## 🛠 Requirements

- PostgreSQL installed
- `psql` command-line tool available
- Basic SQL knowledge

---

## 🗂 Database Schema

### Database Name
```

company

````

### Table: `employees`

| Column | Type | Description |
|------|------|-------------|
| id | SERIAL | Primary Key |
| name | VARCHAR(50) | Employee Name |
| role | VARCHAR(50) | Job Role |
| salary | INT | Monthly Salary |

---

## 🧪 SQL Operations Included

### 1️⃣ Create Database
```sql
CREATE DATABASE company;
````

### 2️⃣ Connect to Database

```sql
\c company
```

### 3️⃣ Create Table

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50),
    salary INT
);
```

### 4️⃣ Insert Records

```sql
INSERT INTO employees (name, role, salary) 
VALUES 
('John Doe', 'Software Engineer', 75000),
('Jane Smith', 'Data Analyst', 65000),
('Bob Johnson', 'Project Manager', 85000);
```

### 5️⃣ Read Data

```sql
SELECT * FROM employees;
```

### 6️⃣ Update Record

```sql
UPDATE employees
SET salary = 80000
WHERE name = 'John Doe';
```

### 7️⃣ Delete Record

```sql
DELETE FROM employees WHERE name = 'Jane Smith';
```

---

## ▶️ How to Run This SQL File

1. Open Command Prompt
2. Navigate to the directory containing the `.sql` file

```bash
cd path\to\sql-file
```

3. Execute the SQL script

```bash
psql -U postgres -f company.sql
```

4. Verify results

```bash
psql -U postgres
\c company
SELECT * FROM employees;
```

---

## ⚠️ Best Practices

* Always use `WHERE` clause with `UPDATE` and `DELETE`
* Test queries using `SELECT` before modifying data
* Keep SQL scripts modular and readable
* Use meaningful table and column names

---

## 📚 Learning Outcome

By completing this project, you will understand:

* PostgreSQL CLI usage
* Database and table creation
* CRUD operations in SQL
* Executing SQL files from command line

---
