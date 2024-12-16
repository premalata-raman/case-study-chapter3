import pandas as pd
import matplotlib.pyplot as plt

# Load the provided data
file_path = r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\csvs\merged_data.csv'
mergeData = pd.read_csv(file_path)

# Convert 'promo_price' and 'price' to numeric
mergeData['promo_price'] = pd.to_numeric(mergeData['promo_price'], errors='coerce')
mergeData['price'] = pd.to_numeric(mergeData['price'], errors='coerce')

# Ensure there are no missing values (optional, handle NaN appropriately)
mergeData = mergeData.dropna(subset=['promo_price', 'price'])

# Calculate discounts as a percentage of the product prices
mergeData['discount_percentage'] = ((mergeData['price'] - mergeData['promo_price']) / mergeData['price']) * 100
mergeData['discount_percentage'] = mergeData['discount_percentage'].clip(lower=0)  # Ensure no negative discounts

# Create bins for the discount percentage
bins = [0, 10, 20, 30, 40, 50, 100]  # Example bins for discounts
labels = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50%+']
mergeData['discount_category'] = pd.cut(mergeData['discount_percentage'], bins=bins, labels=labels, include_lowest=True)

# Count the products in each discount category
discount_distribution = mergeData['discount_category'].value_counts().sort_index()

# Plot the distribution as a line chart
plt.figure(figsize=(10, 6))
plt.plot(discount_distribution.index.astype(str), discount_distribution.values, marker='o', linestyle='-', color='blue')
plt.title('Distribution of Discounts as a Percentage of Product Prices')
plt.xlabel('Discount Percentage Categories')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)

# Add data labels on each point
for x, y in zip(discount_distribution.index, discount_distribution.values):
    plt.text(x, y, f'{int(y):,}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

