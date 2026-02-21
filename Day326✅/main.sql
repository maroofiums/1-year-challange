CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(5)
);

INSERT INTO students VALUES (1, 'Ali', 17, 'A');
INSERT INTO students VALUES (2, 'Sara', 16, 'B');
INSERT INTO students VALUES (3, 'Ahmed', 17, 'C');
INSERT INTO students VALUES (4, 'Hassan', 15, 'B');
INSERT INTO students VALUES (5, 'Amina', 16, 'A');

-- Get all students
SELECT * FROM students;

-- Get names of students older than 16
SELECT name FROM students WHERE age > 16;

-- Mini Challenge: Find all students with grade 'A'
SELECT * FROM students WHERE grade = 'A';

-- Sort students by age ascending
SELECT * FROM students ORDER BY age ASC;

-- Sort students by age descending
SELECT * FROM students ORDER BY age DESC;

-- Count total students
SELECT COUNT(*) AS total_students FROM students;

-- Find youngest student
SELECT MIN(age) AS youngest_student FROM students;

-- Find oldest student
SELECT MAX(age) AS oldest_student FROM students;

-- Average age of students
SELECT AVG(age) AS average_age FROM students;

-- Students whose name starts with 'A'
SELECT * FROM students WHERE name LIKE 'A%';

-- Students aged 16 or 17
SELECT * FROM students WHERE age IN (16, 17);

-- Students aged between 16 and 17
SELECT * FROM students WHERE age BETWEEN 16 AND 17;

-- Unique grades
SELECT DISTINCT grade FROM students;

-- Mini Challenge: Students whose name contains 'h' and age >= 17
SELECT * FROM students WHERE name LIKE '%h%' AND age >= 17;