import pandas as pd
import streamlit as st

# 1. Set up page configuration
st.set_page_config(page_title="E-Commerce Insights", layout="wide")
st.title("E-Commerce Analytics Dashboard")

# 2. Load the clean dataset with cache optimization
@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Online_Retail.csv", dtype={'InvoiceNo': str, 'CustomerID': str})

with st.spinner("Processing massive dataset... Please wait a moment."):
    df = load_data()

# 3. Add interactive sidebar filter for Countries
st.sidebar.header("Filter Options")
unique_countries = sorted(df['Country'].unique())
selected_country = st.sidebar.selectbox("Select a Country:", unique_countries)

# 4. Filter the dataframe based on the user's sidebar choice
df_filtered = df[df['Country'] == selected_country]

# 5. Dynamically calculate metrics based on the filtered data
total_revenue = float(df_filtered['Total_Revenue'].sum())
total_orders = int(df_filtered['InvoiceNo'].nunique())
total_items = int(df_filtered['Quantity'].sum())

# 6. Display high-level business metrics on the dashboard screen
st.success(f"Data filtered successfully for {selected_country}!")
st.subheader(f"Key Business Metrics ({selected_country})")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")

with col2:
    st.metric(label="Total Unique Orders", value=f"{total_orders:,}")

with col3:
    st.metric(label="Total Items Sold", value=f"{total_items:,}")
