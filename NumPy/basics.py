import numpy as np

a=np.array([1,2,3,4,5])
print(a[1])
print(a[1:3])
print(a)
print(type(a))

print(a.size)


a_mult=np.array([[2,4,6],
                [5,10,15],
                [100,200,300]]) #Create a 3x3 array
print(a_mult[0,0])
print(a_mult[1,1])
print(a_mult[0:3])
print(a_mult.shape) #shape of the array
print(a_mult.size)# number of elements in the array
print(a_mult.ndim)# number of dimensions
print(a.dtype)# data type of the array


b=np.zeros((2,2)) #Create a 2x2 array filled with zeros
print(b)

x=np.ones((2,2)) #Create a 2x2 array filled with ones
print(x)
y=np.full((2,2),7) #Create a 2x2 array filled with sevens
print(y)