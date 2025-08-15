import matplotlib.pyplot as plt

# Data
product = [0, 2, 4, 6, 8, 10]
sales = [400, 500, 700, 200, 600, 900]

# First subplot - Line plot
plt.subplot(1, 2, 1)
plt.plot(product, sales, color='green', label='Sales Trend',marker='o')
plt.title('Line Plot of Sales')
plt.xlabel('Product Data')
plt.ylabel('Sales Data')
plt.legend()

# Second subplot - Bar plot
plt.subplot(1, 2, 2)
plt.bar(product, sales, color='gold', label='Sales Data')
plt.title('Bar Plot of Sales')
plt.xlabel('Product Data')
plt.ylabel('Sales Data')
plt.legend()


plt.tight_layout()
# Show the plots
plt.show()
