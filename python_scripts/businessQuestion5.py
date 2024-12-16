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

# Convert the 'date' column to datetime
mergeData['date'] = pd.to_datetime(mergeData['date'])

# Define Black Friday and Christmas date ranges
black_friday_dates = mergeData[
    (mergeData['date'].dt.month == 11) & 
    (mergeData['date'].dt.weekday == 4) & 
    (mergeData['date'].dt.day >= 23) & 
    (mergeData['date'].dt.day <= 29)
]

christmas_dates = mergeData[
    (mergeData['date'].dt.month == 12) & 
    (mergeData['date'].dt.day >= 20) & 
    (mergeData['date'].dt.day <= 26)
]

# Label events and combine datasets
black_friday_dates['event'] = 'Black Friday'
christmas_dates['event'] = 'Christmas'
event_sales = pd.concat([black_friday_dates, christmas_dates])

# Aggregate sales by day for each event type
event_sales['day'] = event_sales['date'].dt.date  # Convert to date format
sales_by_day = event_sales.groupby(['day', 'event'])['promo_price'].sum().unstack()

# Ensure total sales are whole numbers
sales_by_day = sales_by_day.fillna(0).astype(int)

# Plot the comparison of sales between Black Friday and Christmas events
plt.figure(figsize=(12, 6))

# Plot Black Friday sales only on relevant days
if 'Black Friday' in sales_by_day.columns:
    plt.plot(
        sales_by_day.index[sales_by_day['Black Friday'] > 0],
        sales_by_day['Black Friday'][sales_by_day['Black Friday'] > 0],
        marker='o', linestyle='-', label='Black Friday'
    )

# Plot Christmas sales only on relevant days
if 'Christmas' in sales_by_day.columns:
    plt.plot(
        sales_by_day.index[sales_by_day['Christmas'] > 0],
        sales_by_day['Christmas'][sales_by_day['Christmas'] > 0],
        marker='o', linestyle='-', label='Christmas'
    )

# Add data labels on the points
for event in sales_by_day.columns:
    for x, y in zip(
        sales_by_day.index[sales_by_day[event] > 0],
        sales_by_day[event][sales_by_day[event] > 0]
    ):
        plt.text(x, y, f'{y:,}', ha='center', va='bottom', fontsize=10)

plt.title('Sales Comparison: Black Friday vs Christmas Event')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend(title='Event')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
