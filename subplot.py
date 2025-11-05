import matplotlib.pyplot as plt
x = [2,4,6,8,10]
y = [10,3,6,8,2]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Sales.")

x = [1,2,3,5,8,9]
y = [2,12,6,9,3,5]
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Income")
plt.suptitle("Business Report")
plt.show()














