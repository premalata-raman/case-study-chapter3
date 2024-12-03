import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load the provided data
file_path = r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\csvs\merged_data.csv'
mergeData = pd.read_csv(file_path)

# Convert 'date' column to datetime
mergeData['date'] = pd.to_datetime(mergeData['date'], errors='coerce')

# Filter valid dates
mergeData = mergeData.dropna(subset=['date'])

# Add columns for month and day for seasonality analysis
mergeData['month'] = mergeData['date'].dt.month
mergeData['day'] = mergeData['date'].dt.day

# Identify special event periods (e.g., Black Friday, Christmas)
mergeData['event'] = 'Regular'
mergeData.loc[(mergeData['month'] == 11) & (mergeData['day'] >= 23) & (mergeData['day'] <= 29), 'event'] = 'Black Friday'
mergeData.loc[(mergeData['month'] == 12) & (mergeData['day'] >= 20), 'event'] = 'Christmas'

# Group by event type and calculate total sales using 'total_paid'
mergeData['total_paid'] = pd.to_numeric(mergeData['total_paid'], errors='coerce')  # Ensure it's numeric
sales_by_event = mergeData.groupby('event')['total_paid'].sum()

# Plot sales for special events
colors = ['#FF9999', '#FFCC99', '#99CCFF']
plt.figure(figsize=(8, 6))
bars = sales_by_event.plot(kind='bar', color=colors, title="Sales Impact of Seasonality and Special Dates")
plt.xlabel("Event")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

# Explicitly set x-tick labels for the event categories
plt.xticks(ticks=range(len(sales_by_event)), labels=sales_by_event.index)

# Add data labels on top of each bar
for index, value in enumerate(sales_by_event):
    plt.text(index, value, f'{value:,.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Format y-axis to plain numbers
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.tight_layout()
plt.show()
