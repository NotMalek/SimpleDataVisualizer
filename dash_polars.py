import streamlit as st
import polars as pl
import plotly.express as px
import time

start_time = time.time()

# Configuring the page layout to "wide"
st.set_page_config(layout="wide")

# Reading the data directly from the CSV file
df = pl.read_csv('sales_data.csv', separator=';', encoding="ISO-8859-1")

# Convert SALE_DATE to datetime and sort by this column
df = df.with_columns(pl.col("SALE_DATE").str.strptime(pl.datatypes.Datetime, "%Y-%m-%d")).sort("SALE_DATE")

# Generate a MONTH column for filtering purposes
df = df.with_columns(pl.col("SALE_DATE").dt.strftime("%m-%Y").alias("MONTH"))

# Inserting MONTH variable into the Sidebar for selection
month_options = sorted(df.get_column("MONTH").unique().to_list())
month = st.sidebar.selectbox("Select Month", options=month_options)

# Filtering the DataFrame based on the selected month
df_filtered = df.filter(pl.col("MONTH") == month)

# Converting Polars DataFrame to Pandas for Plotly compatibility
df_filtered_pd = df_filtered.to_pandas()

# Creating Dashboard layout
col1, col2, col3, col4 = st.columns(4)
col5, col6 = st.columns(2)

# Revenue by day
fig_date = px.bar(df_filtered_pd, x="SALE_DATE", y="TOTAL_VALUE", color="STORE", title="Revenue by day")
col1.plotly_chart(fig_date, use_container_width=True)

# Revenue by product
fig_prod = px.bar(df_filtered_pd, x="TOTAL_VALUE", y="PRODUCT", color="STORE", title="Revenue by product", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# Total revenue by store
store_total = df_filtered.groupby("STORE").agg([
    pl.sum("TOTAL_VALUE").alias("TOTAL_VALUE")
]).sort("STORE").to_pandas()
fig_store = px.bar(store_total, x="STORE", y="TOTAL_VALUE", title="Revenue by Store")
col3.plotly_chart(fig_store, use_container_width=True)

# Revenue by type of payment
fig_payment = px.pie(df_filtered_pd, values="TOTAL_VALUE", names="PAYMENT_METHOD", title="Revenue by type of payment")
col4.plotly_chart(fig_payment, use_container_width=True)

# Sales quantity by product
product_quantity = df_filtered.groupby("PRODUCT").agg([
    pl.sum("QUANTITY").alias("QUANTITY")
]).sort("PRODUCT").to_pandas()
fig_quantity = px.bar(product_quantity, x="PRODUCT", y="QUANTITY", title="Sales Quantity by Product")
col5.plotly_chart(fig_quantity, use_container_width=True)

# Average unit price by product - ensure UNIT_VALUE is numeric
df_filtered = df_filtered.with_columns(pl.col("UNIT_VALUE").cast(pl.Float64))
product_price = df_filtered.groupby("PRODUCT").agg([
    pl.mean("UNIT_VALUE").alias("UNIT_VALUE")
]).sort("PRODUCT").to_pandas()
fig_price = px.bar(product_price, x="PRODUCT", y="UNIT_VALUE", title="Average Unit Price by Product")
col6.plotly_chart(fig_price, use_container_width=True)


st.write(time.time() - start_time)