import pandas as pd
import matplotlib.pyplot as plt

# Load your Excel data
file_path = r"C:\Users\kodor\Downloads\ANALYTICS-PROJECTS\online_retail.xlsx"
df = pd.read_excel(file_path)

# Add required columns
df['TotalSales'] = df['Quantity'] * df['Price']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')


# Now you can group and perform visualizations
monthly_sales = df.groupby('InvoiceMonth')['TotalSales'].sum()
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Revenue Trend')
plt.ylabel('Total Sales (£)')
plt.xlabel('Month')
plt.grid(True)
plt.show()

top_products = df.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
top_products.plot(kind='barh', color='skyblue')
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales (£)')
plt.gca().invert_yaxis()  # Highest on top
plt.show()

country_sales = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
country_sales.plot(kind='bar', color='orange')
plt.title('Sales by Country')
plt.ylabel('Total Sales (£)')
plt.show()

df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
weekday_sales = df.groupby('DayOfWeek')['TotalSales'].sum()
# Sort days in week order
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_sales = weekday_sales.reindex(days_order)
plt.figure(figsize=(10,6))
weekday_sales.plot(kind='bar', color='green')
plt.title('Sales by Day of Week')
plt.ylabel('Total Sales (£)')
plt.show()

top_products = df.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
top_products.plot(kind='barh', color='skyblue')
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales (£)')
plt.gca().invert_yaxis()  # Highest on top
plt.show()
country_sales = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
country_sales.plot(kind='bar', color='orange')
plt.title('Sales by Country')
plt.ylabel('Total Sales (£)')
plt.show()

df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
weekday_sales = df.groupby('DayOfWeek')['TotalSales'].sum()
# Sort days in week order
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_sales = weekday_sales.reindex(days_order)
plt.figure(figsize=(10,6))
weekday_sales.plot(kind='bar', color='green')
plt.title('Sales by Day of Week')
plt.ylabel('Total Sales (£)')
plt.show()
