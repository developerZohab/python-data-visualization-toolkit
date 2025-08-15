import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load data
df = pd.read_csv('expenses_500_rows.csv')  # Replace with your file path

# Step 2: Clean and prepare
df['Date'] = pd.to_datetime(df['Date'])
total_spending = np.sum(df['Amount'])
print(f"Total spending: ${total_spending}")

# Step 3: Group by category
category_sums = df.groupby('Category')['Amount'].sum()

# Step 4: Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_sums, labels=category_sums.index, autopct='%1.1f%%')
plt.title('Spending by Category')
plt.tight_layout()
plt.show()