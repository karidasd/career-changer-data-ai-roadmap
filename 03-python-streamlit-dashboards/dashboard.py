# dashboard.py
# Interactive Sales Dashboard built with Streamlit & Pandas
# Run locally with: streamlit run dashboard.py

import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Interactive Business Performance Dashboard")
st.markdown("This interactive application demonstrates Pandas filtering and Streamlit visualization components.")

# 2. Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("sales_data.csv")

try:
    df = load_data()

    # 3. Sidebar Filters
    st.sidebar.header("Filter Options")
    all_regions = ["All"] + list(df["Region"].unique())
    selected_region = st.sidebar.selectbox("Select Region", all_regions)

    # Filter Data Frame based on selection
    if selected_region != "All":
        filtered_df = df[df["Region"] == selected_region]
    else:
        filtered_df = df

    # 4. Key Performance Indicators (KPIs)
    total_revenue = filtered_df["Revenue"].sum()
    avg_revenue = filtered_df["Revenue"].mean()
    total_orders = len(filtered_df)

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Revenue ($)", value=f"{total_revenue:,.2f}")
    col2.metric(label="Average Order Value ($)", value=f"{avg_revenue:,.2f}")
    col3.metric(label="Total Orders Placed", value=total_orders)

    st.markdown("---")

    # 5. Charts Grid
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Revenue by Product Category")
        category_sums = filtered_df.groupby("Product_Category")["Revenue"].sum()
        st.bar_chart(category_sums)

    with col_chart2:
        st.subheader("Raw Interactive Data")
        st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error(f"Failed to load dashboard data: {e}")
    st.info("Make sure 'sales_data.csv' is in the same folder as this script.")
