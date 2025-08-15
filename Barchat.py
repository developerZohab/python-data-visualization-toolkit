import matplotlib.pyplot as plt

product =[1,2,3,4,5]
Sales =[200,800,100,500,1000]

#plt.bar(product,Sales, color='orange',label ='Monthly data')
plt.barh(product,Sales, color='orange',label ='Monthly data')
plt.title('January sales Data 2025')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.legend()
plt.show()