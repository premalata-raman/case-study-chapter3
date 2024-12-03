import pandas as pd

# Load the datasets
orderlines = pd.read_csv(r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\orderlines.csv')
orders = pd.read_csv(r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\csvs\orders.csv')
products = pd.read_csv(r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\products.csv')
brands = pd.read_csv(r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\brands.csv')

# Display the first few rows of each DataFrame to understand their structure
print("Orderlines DataFrame:")
print(orderlines.head())

print("\nOrders DataFrame:")
print(orders.head())

print("\nProducts DataFrame:")
print(products.head())

print("\nBrands DataFrame:")
print(brands.head())

# Merge orderlines with products on SKU (assuming SKU links them)
merged_data = orderlines.merge(products, on='sku', how='left')

# Merge with orders using id_order and order_id equivalence
merged_data = merged_data.merge(orders, left_on='id_order', right_on='order_id', how='left')

# Merging with brands (if needed later)
merged_data = merged_data.merge(brands, left_on='sku', right_on='short', how='left')

# Display a sample of the merged dataset to verify structure
print("\nMerged DataFrame:")
print(merged_data.head())

merged_data.to_csv(r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\merged_data.csv', index=False)
