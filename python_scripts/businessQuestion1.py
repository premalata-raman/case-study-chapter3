import pandas as pd
import matplotlib.pyplot as plt

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

# Summarize the count of products in each price range
price_range_summary = mergeData['price_range'].value_counts()

# Display the summary for classification
print(price_range_summary)

# Define custom colors for the bars
colors = ['#FF9999', '#FFCC99', '#FFFF99']

# Create a bar chart for price range distribution
plt.figure(figsize=(8, 6))
bars = price_range_summary.plot(kind='bar', color=colors, title="Distribution of Products by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Number of Products")
plt.xticks(rotation=0)

# Add data labels on top of each bar
for bar in bars.patches:
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # Center the label
        bar.get_height(),                  # Position at the top of the bar
        f'{int(bar.get_height()):,}',      # Format with commas
        ha='center', va='bottom', fontsize=10, fontweight='bold'
    )

plt.tight_layout()
plt.show()
