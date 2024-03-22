# Write a function called "equalsTen"

# def equalsTen(num):
#     if num == 10:
#         return True
#     else:
#         return False

# var = int(input("What is your favorite number? "))
# if equalsTen(var):
#     print(f"Your favorite number is 10!")
# else:
#     print(f"Your favorite number is not 10!")

# example: 
# var output = equalsTen(9);
# print(output); // --> false


# Write a function called "computePerimeterOfARectangle".
# Given a length and a width describing a rectangle, "computePerimeterOfARectangle" returns its perimter.

# def computePerimeterOfARectangle(length, width):
#     return length * 2 + width * 2

# var = int(input("What is the length of the rectangle? "))
# var2 = int(input("What is the width of the rectangle? "))
# print(f"Your perimeter is, {computePerimeterOfARectangle(var, var2)}")

# Example: 
# var output = computePerimeterOfARectangle(5, 2)
# print(output); // --> 14


# Write a function called "computePerimeterOfATriangle".
# Given 3 sides describing a triangle, "computePerimeterOfATriangle" returns its perimter.
# var output = computePerimeterOfATriangle(6, 4, 10);
# print(output); // --> 20

# def computePerimeterOfATriangle(side1, side2, side3):
#     return side1 + side2 + side3

# side1 = int(input("What is the length of the sides of the triangle? "))
# side2 = int(input("What is the length of the sides of the triangle? "))
# side3 = int(input("What is the length of the sides of the triangle? "))

# output = computePerimeterOfATriangle(side1, side2, side3)
# print(output); 

# Write a function called "loneSum".
# Given 3 int values, a b c, return their sum. However, if one of the values 
# is the same as another of the values, it does not count towards the sum.
# output = loneSum(1, 2, 3)
# print(output) --> 6
# output = loneSum(3, 2, 3)
# print(output) --> 2
# output = loneSum(3, 3, 3)
# print(output) --> 0


def loneSum(a, b, c):
    a = int(input("What is the value of a? "))
    b = int(input("What is the value of b? "))
    c = int(input("What is the value of c? "))

    if a == b or a == c or b == c:
        return 0
    else:
        return a + b + c
output = loneSum(1, 2, 3)
print(output) 