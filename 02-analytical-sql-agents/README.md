# Stage 2: Analytical SQL & AI-Augmented Database Querying

SQL is the cornerstone of data analysis. Over 80% of data analyst roles require advanced SQL. This stage moves beyond basic `SELECT` statements and covers **Analytical SQL (CTEs, Window Functions)** and how to leverage LLMs to generate and optimize database queries.

## 🚀 Advanced SQL Concepts to Learn
1.  **Common Table Expressions (CTEs)**: Using `WITH` clauses to build modular, readable, and recursively queryable logic.
2.  **Window Functions**: Compute aggregates across a partition of rows without collapsing them into a single row.
    *   `ROW_NUMBER() / DENSE_RANK() OVER (PARTITION BY ... ORDER BY ...)`: Rank records dynamically.
    *   `LAG() / LEAD() OVER (PARTITION BY ... ORDER BY ...)`: Access data from preceding or following rows (crucial for behavior shifts and funnel conversion rates).
3.  **LLM SQL Co-Pilot**: Prompting AI models with database schemas to auto-generate complex queries and debug performance errors.

---

## 💻 Practice SQL Script: `ecommerce_analytics.sql`
The script [ecommerce_analytics.sql](ecommerce_analytics.sql) contains mock tables representing an e-commerce platform's orders and page views.

### Advanced Analytical Queries to Run:
*   **Query 1: Customer Cohort Repurchase Speed (LAG)**:
    Checks the number of days between a customer's subsequent orders to measure customer retention speed.
*   **Query 2: High-Spender Rankings (DENSE_RANK)**:
    Ranks customers by their total purchases within each region.

---

## 🤖 Prompt Templates: Let AI Write Your SQL Queries
To generate complex SQL queries automatically, provide the LLM with your database schema. Copy and paste this prompt:

```text
Act as a Senior Data Architect. I need a SQL query.
Here is my database schema:

Table: customers
- customer_id (INT, Primary Key)
- sign_up_date (DATE)
- country (VARCHAR)

Table: orders
- order_id (INT, Primary Key)
- customer_id (INT, Foreign Key references customers.customer_id)
- order_date (DATE)
- order_amount (DECIMAL)

Write a PostgreSQL query that:
1. Calculates the customer lifetime value (CLV) - total sum of order_amount for each customer.
2. Identifies the sign-up cohort (YYYY-MM format of sign_up_date).
3. Returns the average CLV partitioned by country and sign-up cohort.
4. Uses CTEs for clarity.

Return only the SQL code inside markdown markers and explain the joins.
```
