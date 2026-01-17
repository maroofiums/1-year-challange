CREATE DATABASE company;

\c company

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50),
    salary INT
);

INSERT INTO employees (name, role, salary) 
VALUES 
('John Doe', 'Software Engineer', 75000),
('Jane Smith', 'Data Analyst', 65000),
('Bob Johnson', 'Project Manager', 85000);


SELECT * FROM employees;



UPDATE employees
SET salary = 80000
WHERE name = 'John Doe';

DELETE FROM employees WHERE name = 'Jane Smith';

