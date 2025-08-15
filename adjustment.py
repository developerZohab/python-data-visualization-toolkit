import matplotlib.pyplot as plt

# Data
product = [1, 2, 3, 4, 5]  # X-axis: Product numbers
sales = [200, 800, 100, 500, 1000]  # Y-axis: Sales values

# Create two subplots (1 row, 2 columns)
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Line plot
ax[0].plot(product, sales, marker='o',color ='blue')
ax[0].set_title("Line Plot")
ax[0].set_xlabel("Product")
ax[0].set_ylabel("Sales")

# Bar plot
ax[1].bar(product, sales,color ='orange')
ax[1].set_title("Bar Plot")
ax[1].set_xlabel("Product")
ax[1].set_ylabel("Sales")

# Show the plots
plt.show()
