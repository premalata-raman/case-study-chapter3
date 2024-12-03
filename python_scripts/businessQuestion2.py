import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged data
mergeData = pd.read_csv(r"C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\csvs\merged_data.csv")

# Adding a column for product classification by price range
def classify_price(price):
    if price < 50:
        return 'Low'
    elif 50 <= price < 200:
        return 'Medium'
    else:
        return 'High'

# Convert 'price' column to numeric, forcing errors to NaN for non-convertible entries
mergeData['price'] = pd.to_numeric(mergeData['price'], errors='coerce')

# Classify products by price range
mergeData['price_range'] = mergeData['price'].apply(classify_price)

# Plot the distribution of product prices by price range with custom colors
plt.figure(figsize=(10, 6))
ax = sns.boxplot(
    data=mergeData,
    x='price_range',
    y='price',
    order=['Low', 'Medium', 'High'],
    palette={'Low': '#FF9999', 'Medium': '#FFFF99', 'High': '#99FF99'}
)

# Add labels for median values
grouped_data = mergeData.groupby('price_range')['price'].median()
for i, median in enumerate(grouped_data.loc[['Low', 'Medium', 'High']]):
    ax.text(
        i, median, f'{median:.2f}', color='black', ha='center', va='bottom', fontsize=10, fontweight='bold'
    )

plt.yscale('log')  # Log scale for better visualization of price differences
plt.title("Price Distribution Across Categories")
plt.xlabel("Price Range")
plt.ylabel("Price (log scale)")
plt.tight_layout()
plt.show()
