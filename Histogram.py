import matplotlib.pyplot as plt

f = [13,5,60,56,78,92,45,16,89,40,56,23,86,47,97,34,65,16,87,46,40,43,40,29,28]

plt.hist(f,bins = 5,color ='green', edgecolor ='Black')
plt.title("Marks Categories")
plt.xlabel('position')
plt.ylabel('Marks')

plt.show()
