import numpy as np

# find most operations on NumPy arrays in the documentation at:
# https://numpy.org/doc/stable/user/quickstart.html
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(a *5) # Element-wise multiplication by 5
print(a + 5) # Element-wise addition of 5
print(a - b) # Element-wise subtraction
print(a + b) # Element-wise addition
print(a / 2) # Element-wise division by 2
print(a * b) # Element-wise multiplication
print(a @ b) # Dot product of a and b
print(a ** 2) # Element-wise squaring
print(b.dot(a)) # Dot product of b and a

print(b.mean()) # Mean of all elements in b
print(b.sum()) # Sum of all elements in b
print(b.min()) # Minimum value in b
print(b.max()) # Maximum value in b
print(b.std()) # Standard deviation of elements in b
print(b.var()) # Variance of elements in b



c=np.array([1,2,3])
d=np.array([[4,5,6],
            [1,2,1]])
print(c + d) #addition in vectorized form
print(c * d) #multiplication in vectorized form

print(np.sqrt(a)) # Square root of each element in a
print(np.sin(b))   # Sine of each element in b

print(np.cos(b))   # Cosine of each element in b
print(np.tan(b))   # Tangent of each element in b