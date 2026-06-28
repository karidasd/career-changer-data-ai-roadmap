# Stage 3: Python Pandas & Interactive Streamlit Dashboards

Jupyter Notebooks are great for research, but in the corporate world, stakeholders need **interactive applications**. In this stage, you will learn how to clean data with **Pandas** and deploy a fully interactive web dashboard in under 50 lines of Python code using **Streamlit**.

## 🚀 Modern Python Concepts to Learn
1.  **Pandas Data Shaping**:
    *   `df.groupby()`: Aggregating business metrics by category.
    *   `df.pivot_table()`: Generating cross-tabs dynamically.
2.  **Streamlit Web Apps**:
    *   `st.dataframe()` & `st.metric()`: Displaying interactive data tables and KPIs.
    *   `st.selectbox()`: Letting users filter data dynamically.
    *   `st.line_chart()` / `st.bar_chart()`: Rendering native interactive visualizations.

---

## 💻 Practice Script: `dashboard.py` & `sales_data.csv`
This folder contains a mock sales dataset [sales_data.csv](sales_data.csv) and a Streamlit dashboard script [dashboard.py](dashboard.py).

### How to Run the Dashboard Locally:
1.  Open your terminal/command prompt.
2.  Install the required packages:
    ```bash
    pip install streamlit pandas
    ```
3.  Run the Streamlit application:
    ```bash
    streamlit run dashboard.py
    ```
4.  A web browser tab will open automatically at `http://localhost:8501` showing your interactive dashboard!

---

## 🤖 Prompt Templates: Let AI Write Your Python Code
Copy and paste this prompt to generate custom Streamlit dashboard code:

```text
Act as a Senior Python Developer. I want to build a Streamlit web application.
My dataset is in 'data.csv' and has these columns:
- Order_Date (format YYYY-MM-DD)
- Product_Category (Text)
- Revenue (Number)
- Region (Text)

Write a clean Streamlit app script in python that:
1. Loads 'data.csv' using Pandas.
2. Displays three key metric widgets at the top: Total Revenue, Average Order Value, and Total Orders.
3. Adds a sidebar selectbox to filter the dataset by Region (include an 'All' option).
4. Plots an interactive bar chart of Revenue by Product_Category.
5. Displays the filtered dataframe in an interactive table at the bottom.

Include error handling and code comments explaining the Streamlit layout.
```
