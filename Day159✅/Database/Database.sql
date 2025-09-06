-- USERS table
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- PRODUCTS table
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

-- ORDERS table (One-to-Many: users → orders)
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO users (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

INSERT INTO products (id, name, price) VALUES
(1, 'Laptop', 1200.00),
(2, 'Phone', 800.00),
(3, 'Headphones', 150.00);

INSERT INTO orders (id, user_id, product_id, quantity) VALUES
(1, 1, 1, 1),  -- Alice bought 1 Laptop
(2, 1, 3, 2),  -- Alice bought 2 Headphones
(3, 2, 2, 1);  -- Bob bought 1 Phone

SELECT u.name AS user, p.name AS product, o.quantity
FROM orders o
INNER JOIN users u ON o.user_id = u.id
INNER JOIN products p ON o.product_id = p.id;

SELECT u.name AS user, p.name AS product, o.quantity
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
LEFT JOIN products p ON o.product_id = p.id;

SELECT u.name AS user, p.name AS product, o.quantity
FROM orders o
RIGHT JOIN products p ON o.product_id = p.id
LEFT JOIN users u ON o.user_id = u.id;

SELECT u.name AS user, p.name AS product, o.quantity
FROM users u
FULL JOIN orders o ON u.id = o.user_id
FULL JOIN products p ON o.product_id = p.id;

SELECT u.name, p.name
FROM users u
CROSS JOIN products p;

-- Add manager_id column
ALTER TABLE users ADD manager_id INT;

-- Update with fake hierarchy
UPDATE users SET manager_id = 1 WHERE id IN (2,3); -- Alice manages Bob + Charlie

Self join
SELECT e.name AS employee, m.name AS manager
FROM users e
LEFT JOIN users m ON e.manager_id = m.id;
