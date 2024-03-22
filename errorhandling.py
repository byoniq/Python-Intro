# Exercise 1 
# Here's an example of using try, else, and finally blocks in Python:

print("Exercise 1")


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid data types for operands. Both must be numbers.")
    else:
        print(f"The result of {a} / {b} is: {result}")
    finally:
        print("This will always be executed, regardless of exceptions.")

print("Example 1: Valid division")
divide_numbers(10, 2)
print("\nExample 2: Division by zero")
divide_numbers(10, 0)
print("\nExample 3: Invalid data types")
divide_numbers("10", 2)

#Exercise 2


print("Exercise 2")


# Custom exception for a specific error condition
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be a positive integer."):
        self.age = age
        self.message = message
        super().__init__(message)

# Function that raises the custom exception
def validate_age(age):
    if not isinstance(age, int) or age < 0:
        raise InvalidAgeError(age)

# Example usage
try:
    validate_age(25)
    print("Age is valid.")
except InvalidAgeError as e:
    print(f"Error: {e.message} The provided age was {e.age}.")

try:
    validate_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e.message} The provided age was {e.age}.")

try:
    validate_age("thirty")
except InvalidAgeError as e:
    print(f"Error: {e.message} The provided age was {e.age}.")