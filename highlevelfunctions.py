# High level functions
# Definition: Functions that operate on other functions.

def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

result1 = apply_operation(add, 5, 3)
result2 = apply_operation(multiply, 4, 2)
print(result1) # Output: 8
print(result2) # Output: 8

#lambda functions 
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers)) # [1, 4, 9, 16, 25]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # [2, 4]

#map functions 
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x**2
squared = list(map(square, numbers)) # [1, 4, 9, 16, 25]

#filter function 
numbers = [1, 2, 3, 4, 5]
def is_even(x):
    return x % 2 == 0
even_numbers = list(filter(is_even, numbers)) # [2, 4]


#reduce function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def add(x, y):
    return x + y
sum_of_numbers = reduce(add, numbers) # 15