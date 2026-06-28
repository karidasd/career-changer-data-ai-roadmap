-- ecommerce_analytics.sql
-- Database Setup and Analytical Queries for Practice
-- Runs natively in SQLite, PostgreSQL, or MySQL.

-- 1. Create Tables
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT,
    sign_up_date DATE
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    amount REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

-- 2. Insert Mock Data
INSERT INTO customers (customer_id, name, country, sign_up_date) VALUES
(101, 'Alice Smith', 'USA', '2026-01-10'),
(102, 'Bob Jones', 'UK', '2026-01-15'),
(103, 'Charlie Brown', 'USA', '2026-01-20'),
(104, 'David Evans', 'Germany', '2026-02-01'),
(105, 'Emma Garcia', 'UK', '2026-02-05');

INSERT INTO orders (order_id, customer_id, order_date, amount) VALUES
(1, 101, '2026-01-12', 150.00),
(2, 101, '2026-01-25', 85.50),
(3, 102, '2026-01-16', 320.00),
(4, 103, '2026-01-21', 45.00),
(5, 101, '2026-02-10', 210.00),
(6, 104, '2026-02-03', 95.00),
(7, 104, '2026-02-18', 115.00),
(8, 102, '2026-02-20', 140.00),
(9, 105, '2026-02-10', 300.00);


-- 3. Advanced Analytical Query 1: Repurchase Interval (using LAG Window Function)
-- This calculates the days elapsed between a customer's subsequent orders.
WITH purchase_history AS (
    SELECT 
        customer_id,
        order_date,
        amount,
        LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_order_date
    FROM orders
)
SELECT 
    customer_id,
    order_date,
    previous_order_date,
    -- Julian day calculation for SQLite; replaces DATEDIFF() in SQL Server/Postgres
    CAST(julianday(order_date) - julianday(previous_order_date) AS INTEGER) AS days_between_purchases
FROM purchase_history
WHERE previous_order_date IS NOT NULL;


-- 4. Advanced Analytical Query 2: Regional Spending Ranks (using DENSE_RANK Window Function)
-- This ranks customers based on total expenditures grouped by their country.
WITH customer_spending AS (
    SELECT 
        c.customer_id,
        c.name,
        c.country,
        SUM(o.amount) AS total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name, c.country
)
SELECT 
    country,
    name,
    total_spent,
    DENSE_RANK() OVER (PARTITION BY country ORDER BY total_spent DESC) AS spend_rank_in_country
FROM customer_spending
ORDER BY country, spend_rank_in_country;
