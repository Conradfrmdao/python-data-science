import numpy as np
a=np.array([[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]])
np.save('my_array.npy',a)  # Save the array to a file
b=np.load('my_array.npy')  # Load the array from the file
print(b)  # Print the loaded array


#using csv format
np.savetxt('my_array.csv', a, delimiter=',')  # Save the array to a CSV file
c=np.loadtxt('my_array.csv', delimiter=',')  # Load the array from the CSV file
print(c)  # Print the loaded array