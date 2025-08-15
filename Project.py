import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load and explore data
f = pd.read_csv('expenses_500_rows.csv')
print("First 5 rows of the dataset:")
print(f.head())  # Preview first 5 rows instead of entire DataFrame
print("\nMissing values:")
print(f.isnull().sum())  # Check for missing values
f.info()  # Display DataFrame info (no need to assign to a variable)

# Step 2: Data preparation
f['Date'] = pd.to_datetime(f['Date'])  # Convert Date column to datetime
f['Percentage'] = (f['Amount'] / f['Amount'].sum()) * 100  # Calculate percentage of total spending

# Step 3: Calculations
total_spending = np.sum(f['Amount'])
print(f"\nTotal spending: ${total_spending:.2f}")
category_means = np.array(f.groupby('Category')['Amount'].mean())
print("\nAverage spending per category:", category_means)
max_values = f.max()
print("\nMaximum values in each column:\n", max_values)

# Step 4: Group data for visualizations
category_sums = f.groupby('Category')['Amount'].sum()  # Sum of spending by category
daily_sums = f.groupby('Date')['Amount'].sum()  # Sum of spending by date

# Step 5: Plotting
# Pie chart for category-wise spending
plt.figure(figsize=(8, 8))
plt.pie(category_sums, labels=category_sums.index, autopct='%1.1f%%', colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD'])
plt.title('Spending Breakdown by Category')
plt.savefig('category_pie.png')
plt.show()

# Line plot for daily spending
plt.figure(figsize=(10, 5))
plt.plot(daily_sums.index, daily_sums.values, label='Daily Spending', color='#4ECDC4')
plt.xlabel('Date')
plt.ylabel('Amount ($)')
plt.title('Daily Spending Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_spending.png')
plt.show()