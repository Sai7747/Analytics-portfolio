import pandas as pd

# Load the cleaned Excel file
file_path = r"C:\Users\kodor\Downloads\ANALYTICS-PROJECTS\online_retail.xlsx"
df = pd.read_excel(file_path)

# Add TotalSales
df['TotalSales'] = df['Quantity'] * df['Price']

# Convert InvoiceDate to pandas datetime if not already
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Add additional datetime features
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
df['Year'] = df['InvoiceDate'].dt.year
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()


# Load your cleaned Excel data
file_path = r"C:\Users\kodor\Downloads\ANALYTICS-PROJECTS\online_retail.xlsx"
df = pd.read_excel(file_path)

df['TotalSales'] = df['Quantity'] * df['Price']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
df['Year'] = df['InvoiceDate'].dt.year
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
