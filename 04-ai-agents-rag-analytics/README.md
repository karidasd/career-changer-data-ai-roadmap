# Stage 4: AI Agents & Conversational RAG Analytics

The next frontier of data analytics is **AI Agents**. Instead of writing SQL or Python manually, we build agentic systems that translate natural language questions directly into executable queries, run them against databases, and explain the results.

This stage covers how to build a **Conversational SQL Agent (Text-to-SQL)** using Python.

## 🚀 Next-Gen AI Analytics Concepts to Learn
1.  **Text-to-SQL Translation**: Prompting LLMs to read database schemas and generate syntactically correct SQL statements.
2.  **Autonomous Tool Use**: Letting an AI model choose when to query a database to answer a user's question.
3.  **Retrieval-Augmented Generation (RAG)**: Feeding structured data query results back into the LLM context to ensure responses are grounded in database truth (preventing hallucination).

---

## 💻 Practice Script: `conversational_sql_agent.py`
The script [conversational_sql_agent.py](conversational_sql_agent.py) is a self-contained simulation of a **Text-to-SQL Agent**. 

It sets up an in-memory SQLite database, receives a natural language question (e.g., "Which country has the highest spending customers?"), uses a simulated LLM schema translator to write the SQL query, executes it on the database, and summarizes the findings in plain English.

### How to Run:
```bash
python conversational_sql_agent.py
```

---

## 🤖 Prompt Templates: Let AI act as a SQL Agent
Copy and paste this prompt to configure an LLM system prompt that generates SQL queries:

```text
You are a Text-to-SQL translation agent. 
Database Engine: SQLite
Database Schema:
Table: customers (customer_id INT, name TEXT, country TEXT)
Table: orders (order_id INT, customer_id INT, order_date DATE, amount REAL)

Your task:
1. Receive a user's question in natural language.
2. Convert it into a valid SQL query.
3. Output ONLY the raw SQL query. Do not wrap it in markdown or add explanations.

User Question: "Which customer in the UK spent the most money in total?"
SQL Query:
```
