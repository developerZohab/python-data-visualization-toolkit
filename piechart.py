import matplotlib.pyplot as plt

# Data
x = ["Ali", "Mussa", "Bill", "Babu", "Jabi", "Hida"]  # Labels
y = [34, 50, 10, 83, 20, 67]                         # Values

# Pie chart
plt.pie(y,labels=x,colors=['Gray', 'gold', 'silver', 'green', 'blue', 'pink'],autopct='%1.1f%%')  # Percentage display

# Title
plt.title('Students Result')

# Show chart
plt.show()
