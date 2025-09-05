import numpy as np

x = np.array([10 , 20])

print(x[0] , x[1])
print(x.ndim , x.shape , x.size)


y = np.array([[30 , 40] , [50 , 60]])

print(y[0 , 0] , y[0,1], y[1 , 0] , y[1 , 1])
print(y.ndim , y.shape , y.size)


z = np.array([[[70 ,80] , [90 , 100]]])

print(z[0 , 0 , 0] , z[0,0,1] , z[0 , 1 ,0] , z[0 , 1 , 1])
print(z.ndim , z.shape , z.size)