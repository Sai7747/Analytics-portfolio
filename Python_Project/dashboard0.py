import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r"C:\Users\kodor\Downloads\ANALYTICS-PROJECTS\online_retail.xlsx"
df = pd.read_excel(file_path)

# Data preprocessing
df['TotalSales'] = df['Quantity'] * df['Price']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()

# Define chart functions
def plot_monthly_sales():
    monthly_sales = df.groupby('InvoiceMonth')['TotalSales'].sum()
    fig, ax = plt.subplots()
    monthly_sales.plot(kind='line', marker='o', ax=ax)
    ax.set_title('Monthly Revenue Trend')
    ax.set_ylabel('Total Sales (£)')
    ax.set_xlabel('Month')
    ax.grid(True)
    return fig

def plot_top_products():
    top_products = df.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    top_products.plot(kind='barh', color='skyblue', ax=ax)
    ax.set_title('Top 10 Products by Sales')
    ax.set_xlabel('Total Sales (£)')
    ax.invert_yaxis()
    return fig

def plot_sales_by_country():
    country_sales = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    country_sales.plot(kind='bar', color='orange', ax=ax)
    ax.set_title('Sales by Country')
    ax.set_ylabel('Total Sales (£)')
    return fig

def plot_sales_by_weekday():
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_sales = df.groupby('DayOfWeek')['TotalSales'].sum().reindex(days_order)
    fig, ax = plt.subplots()
    weekday_sales.plot(kind='bar', color='green', ax=ax)
    ax.set_title('Sales by Day of Week')
    ax.set_ylabel('Total Sales (£)')
    return fig

# Streamlit dashboard layout
st.title('Online Retail Sales Dashboard')

st.header('Monthly Sales')
st.pyplot(plot_monthly_sales())

st.header('Top 10 Products')
st.pyplot(plot_top_products())

st.header('Sales by Country')
st.pyplot(plot_sales_by_country())

st.header('Sales by Day of Week')
st.pyplot(plot_sales_by_weekday())
