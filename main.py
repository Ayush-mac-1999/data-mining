import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "OnlineRetail.csv"  # Replace with the path to your dataset
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Check the dataset structure
print("Dataset Info:")
print(data.info())
#  Load Dataset:

# The dataset is loaded into a Pandas DataFrame.
# We use encoding='ISO-8859-1' to handle special characters in product descriptions.


# Handle missing values
data = data.dropna(subset=['CustomerID'])  # Drop rows without CustomerID
# Rows with missing CustomerID are dropped since they cannot be attributed to any user.
# Clean Invalid Data:

# Remove negative quantities (returns or refunds)
data = data[data['Quantity'] > 0]
# Negative quantities indicate returns, which we exclude for now.
# Feature Engineering:

# Add a new feature: TotalPrice
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']
# TotalPrice: Helps analyze revenue per transaction.
# Convert Date Columns:

# Convert InvoiceDate to datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Convert Date Columns:

# Parsing dates enables time-series analysis and feature extraction like "days since last purchase.

print("\nCleaned Dataset:")
print(data.head())




# Daily sales trend
data['Date'] = data['InvoiceDate'].dt.date
daily_sales = data.groupby('Date')['TotalPrice'].sum()

plt.figure(figsize=(10, 6))
daily_sales.plot(kind='line', title='Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# Top 10 products by sales
top_products = data.groupby('StockCode')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product Code')
plt.show()







