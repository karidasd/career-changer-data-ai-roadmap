-- analytical_sql_template.sql
-- Template for Custom Portfolio SQL Analytics Queries
-- INSTRUCTIONS: 
-- 1. Replace placeholder table names (YOUR_TABLE_NAME) and columns with your own domain data structures.
-- 2. Execute on your SQLite, PostgreSQL, or Snowflake databases.

-- ========================================================
-- 📊 TEMPLATE 1: COHORT OVER-TIME RETENTION (LAG WINDOW FUNCTION)
-- ========================================================
-- Purpose: Calculate differences (intervals) between recurring transactions.
WITH custom_behavior_history AS (
    SELECT 
        user_id_column,          -- Change to your User ID column name
        transaction_date_column, -- Change to your Date column name
        value_column,            -- Change to your numeric Value column name
        -- LAG fetches the date of the user's previous transaction
        LAG(transaction_date_column) OVER (
            PARTITION BY user_id_column 
            ORDER BY transaction_date_column
        ) AS previous_event_date
    FROM YOUR_TABLE_NAME        -- Change to your database table name
)
SELECT 
    user_id_column,
    transaction_date_column,
    previous_event_date,
    -- Compute the elapsed time. (For Postgres/Redshift: transaction_date_column - previous_event_date)
    -- In SQLite, julian day difference can be calculated as follows:
    CAST(julianday(transaction_date_column) - julianday(previous_event_date) AS INTEGER) AS interval_days
FROM custom_behavior_history
WHERE previous_event_date IS NOT NULL;


-- ========================================================
-- 📊 TEMPLATE 2: DENSE RANK ANALYSIS (PARTITIONED RANKINGS)
-- ========================================================
-- Purpose: Rank performance values within different categories (e.g. Sales by Region, Audits by Department).
WITH aggregated_metrics AS (
    SELECT 
        category_column,        -- Change to your Category column name (e.g. Region, Department)
        item_name_column,       -- Change to your Item column name (e.g. Salesperson, Product)
        SUM(value_column) AS total_aggregate_value
    FROM YOUR_TABLE_NAME        -- Change to your database table name
    GROUP BY category_column, item_name_column
)
SELECT 
    category_column,
    item_name_column,
    total_aggregate_value,
    -- DENSE_RANK ranks items without skipping numbers in case of duplicate scores
    DENSE_RANK() OVER (
        PARTITION BY category_column 
        ORDER BY total_aggregate_value DESC
    ) AS rank_within_category
FROM aggregated_metrics;
