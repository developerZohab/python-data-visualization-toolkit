import matplotlib.pyplot as plt

x = ["Ali","Mussa","Bill","Babu","jabi","hida"]
y = [34,50,10,83,20,67]

plt.plot(x,y ,color ='blue',linestyle='dotted',marker ='o',linewidth=2 ,label ='2025 result') # plt.plot(Horizontal,Vertical)
plt.title("Monthly Report")
plt.xlabel("Students name")
plt.ylabel("Marks")
plt.legend(loc ='upper left', fontsize=10)
plt.grid(color ='black',linestyle ='--')
plt.xlim(0,6)
plt.ylim(0,100)
plt.xticks([0,1,2,3,4,5],['R0','R1','R2','R3','R4','R5'])
plt.yticks([0,20,40,60,80,100],['very bad','bad','Average','good','very good','Excellent'])

plt.show()