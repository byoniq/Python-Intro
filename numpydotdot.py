import numpy as np
import numpy.random as random

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# C = np.dot(A, B)
# print(C)

def matrix_multiplication(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

#Numpy array

matrix_a = [1, 2, 3], [4, 5, 6]

matrix_b = [7, 8], [9, 10], [11, 12]

#Results with Numpy
matrix_c = np.dot(matrix_a, matrix_b)
print(matrix_c)

#For loop through the matrix

# matrix_a = np.array([[1, 2], [3, 4]])

# matrix_b = np.array([[5, 6], [7, 8]])



myList = random.randint(300, size=3)
print(myList)

x = random.choice([3, 5, 7, 9])
print(x)

x - random.randint(3, 10, size=(3, 5))
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)