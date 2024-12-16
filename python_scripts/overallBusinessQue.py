import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the uploaded dataset
file_path = r'C:\Users\prema\Desktop\WBS DA06\DA06 exercises\case study csv\csvs\merged_data.csv'
data = pd.read_csv(file_path)

# Step 2: Ensure the 'date' column exists and is converted to datetime
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data = data.dropna(subset=['date'])  # Drop rows with invalid dates
else:
    raise ValueError("Error: 'date' column not found in the dataset.")

# Step 3: Extract month and year from the date
data['year_month'] = data['date'].dt.to_period('M')

# Step 4: Identify special days (e.g., weekends: Saturday, Sunday)
data['day_of_week'] = data['date'].dt.dayofweek  # Monday=0, Sunday=6
data['is_special_day'] = data['day_of_week'].isin([5, 6])  # Weekend = special day

# Step 5: Aggregate revenue by month, year, and day type
if 'total_paid' in data.columns:
    revenue_summary = (
        data.groupby(['year_month', 'is_special_day'])['total_paid']
        .sum()
        .reset_index()
    )
    revenue_summary['year_month'] = revenue_summary['year_month'].astype(str)
    revenue_summary['day_type'] = revenue_summary['is_special_day'].replace(
        {True: 'Special Days', False: 'Regular Days'}
    )
else:
    raise ValueError("Error: 'total_paid' column not found in the dataset.")

# Step 6: Pivot data for visualization
revenue_pivot = revenue_summary.pivot(
    index='year_month', columns='day_type', values='total_paid'
).fillna(0)

# Step 7: Plot the data
plt.figure(figsize=(14, 8))
revenue_pivot.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title('Total Revenue: Special Days vs Regular Days by Month and Year')
plt.xlabel('Month and Year')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.legend(title='Day Type')
plt.tight_layout()
plt.show()
