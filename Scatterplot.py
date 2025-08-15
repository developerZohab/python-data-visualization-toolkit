import matplotlib.pyplot as plt

f = [1,2,3,4,5,6]
d = [10,23,4,95,56,89]

#plt.scatter(f,d, color ='blue',marker='o',label='Data patterns')
plt.scatter([1,2,3,4,5],[20,40,45,60,80], color ='blue',label ='Class  1')
plt.scatter([1,2,3,4,5],[30,50,75,70,90], color ='green',label ='Class  2')
plt.xlabel('Roll no')
plt.ylabel('Obtained Marks')
plt.title('Result')
plt.legend()
plt.grid()

plt.show()