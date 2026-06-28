# my_first_dashboard_template.py
# Streamlit Web App Template for Custom Student Portfolios
# INSTRUCTIONS: 
# 1. Place your own dataset (CSV format) in this folder.
# 2. Update CSV_FILENAME, COLUMN_TO_FILTER, and COLUMN_TO_AGGREGATE variables below.
# 3. Run: streamlit run my_first_dashboard_template.py

import streamlit as st
import pandas as pd

# ==========================================
# 🛠️ CONFIGURATION - EDIT THESE VARIABLES
# ==========================================
CSV_FILENAME = "your_dataset.csv"  # Rename to your CSV file
COLUMN_TO_FILTER = "category"     # Categorical column for the sidebar filter
COLUMN_TO_AGGREGATE = "revenue"   # Numerical column to sum/average
# ==========================================

st.set_page_config(page_title="My Custom Portfolio Dashboard", layout="wide")
st.title("📊 My Domain Data Analysis Dashboard")
st.markdown("This interactive dashboard was built using the *Career Changer Data & AI Analyst Roadmap* template.")

# Load Data
@st.cache_data
def load_custom_data():
    try:
        return pd.read_csv(CSV_FILENAME)
    except FileNotFoundError:
        # Fallback dummy data if custom CSV not found
        st.warning(f"Could not find '{CSV_FILENAME}'. Showing mock data instead. Please swap the CSV file to build your portfolio.")
        return pd.DataFrame({
            COLUMN_TO_FILTER: ["Category A", "Category B", "Category A", "Category C"],
            COLUMN_TO_AGGREGATE: [100, 250, 150, 400],
            "Region": ["North", "South", "North", "East"]
        })

df = load_custom_data()

# Sidebar Filter
st.sidebar.header("Dashboard Filters")
unique_items = ["All"] + list(df[COLUMN_TO_FILTER].unique())
selected_value = st.sidebar.selectbox(f"Filter by {COLUMN_TO_FILTER.title()}", unique_items)

# Filter logic
if selected_value != "All":
    filtered_df = df[df[COLUMN_TO_FILTER] == selected_value]
else:
    filtered_df = df

# Metrics row
st.subheader("Key Performance Indicators")
total_val = filtered_df[COLUMN_TO_AGGREGATE].sum()
avg_val = filtered_df[COLUMN_TO_AGGREGATE].mean()
record_count = len(filtered_df)

col1, col2, col3 = st.columns(3)
col1.metric(label=f"Total {COLUMN_TO_AGGREGATE.title()}", value=f"{total_val:,.2f}")
col2.metric(label=f"Average {COLUMN_TO_AGGREGATE.title()}", value=f"{avg_val:,.2f}")
col3.metric(label="Record Count", value=record_count)

st.markdown("---")

# Charts Row
st.subheader("Data Visualization")
chart_col, table_col = st.columns(2)

with chart_col:
    # Group by the filter column and sum the numeric values
    chart_data = filtered_df.groupby(COLUMN_TO_FILTER)[COLUMN_TO_AGGREGATE].sum()
    st.bar_chart(chart_data)

with table_col:
    st.dataframe(filtered_df, use_container_width=True)
