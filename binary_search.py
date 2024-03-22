def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        print(f"Checking index {mid} with value {arr[mid]}")

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Input range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Generate the list within the given range
arr = list(range(start, end + 1))

# Number to find
target = int(input("Enter the number to find: "))

# Perform binary search
result = binary_search(arr, target)

if result != -1:
    print(f"The number {target} is present at index {result}.")
else:
    print(f"The number {target} is not present in the list.")
