# conversational_sql_agent.py
# Conversational SQL Agent Simulation (Text-to-SQL & RAG)
# This script demonstrates how AI agents translate natural language into SQL, query databases, and return summaries.

import sqlite3
import pandas as pd

def setup_demo_database():
    """Sets up an in-memory database representing an e-commerce platform."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT
    )""")
    
    cursor.execute("""
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount REAL,
        category TEXT
    )""")
    
    # Insert data
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", [
        (1, 'Alice', 'USA'),
        (2, 'Bob', 'UK'),
        (3, 'Charlie', 'Germany'),
        (4, 'Diana', 'USA')
    ])
    
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", [
        (101, 1, 250.0, 'Electronics'),
        (102, 1, 80.0, 'Office'),
        (103, 2, 450.0, 'Electronics'),
        (104, 3, 120.0, 'Furniture'),
        (105, 4, 310.0, 'Furniture')
    ])
    
    conn.commit()
    return conn

# Simulated LLM Schema Translation Engine (Text-to-SQL mapping)
SIMULATED_LLM_SQL = {
    "what is our total sales revenue?": 
        "SELECT SUM(amount) AS total_revenue FROM orders;",
    "which country has the highest spending customers?": 
        "SELECT c.country, SUM(o.amount) AS total_spent FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.country ORDER BY total_spent DESC LIMIT 1;",
    "list our orders in the electronics category": 
        "SELECT order_id, customer_id, amount FROM orders WHERE category = 'Electronics';"
}

def ask_sql_agent(conn, user_question):
    """Orchestrates the Text-to-SQL and RAG pipeline."""
    print(f"\nUser Question: '{user_question}'")
    
    # Normalize question
    normalized_q = user_question.lower().strip().replace("?", "")
    
    # Step 1: Simulated LLM converts text to SQL
    if normalized_q in SIMULATED_LLM_SQL:
        generated_sql = SIMULATED_LLM_SQL[normalized_q]
    else:
        print("Agent Status: Question not in mock LLM dictionary. Returning fallback query.")
        generated_sql = "SELECT * FROM orders LIMIT 2;"
        
    print(f"🤖 Agent (Text-to-SQL): Generated SQL Query:\n   {generated_sql}")
    
    # Step 2: Agent executes query on database
    try:
        df_result = pd.read_sql_query(generated_sql, conn)
        raw_result_str = df_result.to_string(index=False)
        print(f"📦 Database Result:\n{df_result.to_string(index=False)}")
    except Exception as e:
        print(f"Database Query Error: {e}")
        return

    # Step 3: RAG Synthesis (feed SQL results back to LLM to formulate natural response)
    # We simulate LLM formatting the response based on the fetched data
    if "total_revenue" in df_result.columns:
        total = df_result.iloc[0]['total_revenue']
        response = f"Based on the database records, our total sales revenue is ${total:,.2f} across all product categories."
    elif "country" in df_result.columns:
        country = df_result.iloc[0]['country']
        spent = df_result.iloc[0]['total_spent']
        response = f"According to the customer database, the highest spending country is {country} with a total expenditure of ${spent:,.2f}."
    else:
        response = f"I found the requested records in the database:\n{raw_result_str}"
        
    print(f"💬 Agent Response: {response}")
    print("-" * 60)

def main():
    conn = setup_demo_database()
    
    print("=" * 60)
    print("🤖 RUNNING CONVERSATIONAL SQL AGENT DEMO")
    print("=" * 60)
    
    # Query 1
    ask_sql_agent(conn, "What is our total sales revenue?")
    
    # Query 2
    ask_sql_agent(conn, "Which country has the highest spending customers?")
    
    # Query 3
    ask_sql_agent(conn, "List our orders in the Electronics category")
    
    conn.close()

if __name__ == "__main__":
    main()
