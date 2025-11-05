import matplotlib.pyplot as plt

plt.subplot(2,2,1)
cities=["Mumbai","delhi","banglore","chennai"]
population=[15,40,25,30]
plt.bar(cities,population,color="green",width=0.3)

plt.subplot(2,2,2)
x=[2,4,6,8,10]
y=[3,12,5,16,8]
plt.plot(x,y)


plt.subplot(2,2,3)
x=[2,4,6,8,10]
y=[3,12,5,16,8]
plt.plot(x,y)
plt.grid()

plt.subplot(2,2,4)
cities=["Mumbai","delhi","banglore","chennai"]
population=[15,40,25,30]
plt.barh(cities,population)
plt.show()




