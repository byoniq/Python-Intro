import math

def binary_search(target, start=3, end=math.pi):
    """
    Performs a binary search for the target value within the range [start, end).
    Returns the index if the target is found, or -1 if not found.
    """
    while start < end:
        mid = start + (end - start) / 2
        if mid == target:
            return mid
        elif mid < target:
            start = mid + 1e-15  # Adjust start to avoid infinite loop
        else:
            end = mid

    # Target value not found
    return -1

# Get user input
user_input = float(input("Enter a value between 0 and π: "))

# Perform binary search
result = binary_search(user_input)

if result == -1:
    print(f"The value {user_input} is not within the range 0 to π.")
else:
    print(f"The value {user_input} is within the range 0 to π.")