import pandas as pd

# Load the provided data
file_path = r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\csvs\merged_data.csv'
mergeData = pd.read_csv(file_path)

# Convert 'promo_price' and 'price' to numeric
mergeData['promo_price'] = pd.to_numeric(mergeData['promo_price'], errors='coerce')
mergeData['price'] = pd.to_numeric(mergeData['price'], errors='coerce')

# Ensure there are no missing values (optional, handle NaN appropriately)
mergeData = mergeData.dropna(subset=['promo_price', 'price'])

# Calculate discounted products
mergeData['discounted'] = mergeData['promo_price'] < mergeData['price']

# Count discounted and non-discounted products
discount_summary = mergeData['discounted'].value_counts()

# Calculate percentage of discounted products
total_products = len(mergeData)
discount_percentage = (discount_summary[True] / total_products) * 100 if True in discount_summary else 0

# Print results in a clear format
print(f"Number of discounted products: {discount_summary[True]:,}")
print(f"Number of non-discounted products: {discount_summary[False]:,}")
print(f"Percentage of discounted products: {discount_percentage:.2f}%")
