import numpy as np
a=np.array([1,2,3,4,5])

a=np.append(a,[6,7,8])  # Append elements to the array
print(a)

a=np.delete(a,0)
print(a)  # Delete the first element of the array


b= np.array([[1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12]])
print(b)
print(b.reshape(3,4))  # Reshape the array to 3x4


z=np.array([[3,9,12],
            [1,2,3],
            [4,5,6],
            [7,8,9]])
y=np.concatenate((b,z), axis=0)  # Concatenate arrays along the first axis(rows)
print(y)
print(np.concatenate((b,z), axis=1))  # Concatenate arrays along the second(columns)