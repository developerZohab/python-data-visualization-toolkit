import matplotlib.pyplot as plt

# Data
x = ["Ali", "Mussa", "Bill", "Babu", "Jabi", "Hida"]  # Labels
y = [34, 50, 10, 83, 20, 67]                         # Values

plt.bar(x,y, color='orange',label ='Monthly data')
plt.title('Students Result')
plt.xlabel('Students names')
plt.ylabel('marks obtained')

plt.tight_layout()
plt.savefig('bar.jpg', dpi =300 ,bbox_inches ='tight')
plt.show()