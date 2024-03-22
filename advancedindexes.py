# data = [
#     ["John", 25, "Software Engineer", "New York"],
#     ["Emily", 32, "Marketing Manager", "Los Angeles"],
#     ["Michael", 28, "Data Analyst", "Chicago"],
#     ["Sarah", 41, "Project Manager", "San Francisco"],
#     ["David", 35, "Graphic Designer", "Boston"]
# ]


# print(data[0])  # Output: ['John', 25, 'Software Engineer', 'New York']
# print()

# print(data[1][2])  # Output: 'Marketing Manager'
# print()

# for person in data:
#     print("Name:", person[0])
#     print("Age:", person[1])
#     print("Job Title:", person[2])
#     print("City:", person[3])
#     print()  # Print an empty line for better readability


# import numpy as np

# # Student grades data (randomly generated)
# np.random.seed(42)
# grades = np.random.randint(60, 100, size=(20, 4))
# print("Student Grades Data:")
# print(grades)

# # Task 1: Average Grade for Each Student
# average_grades = np.mean(grades, axis=1)
# print(f"Task 1: Average Grade for Each Student: {average_grades}")

# # Task 2: Highest Grade in Each Subject
# highest_grades = np.max(grades, axis=0)
# print(f"Task 2: Highest Grade in Each Subject: {highest_grades}")

# # Task 3: Students who have failed in at least one subject
# failed_students = np.where(np.any(grades < 70, axis=1))[0]
# print(f"Task 3: Students who have failed in at least one subject: {failed_students}")

# # Task 4: Overall Average Grade for the Class
# overall_average = np.mean(grades)
# print(f"Task 4: Overall Average Grade for the Class: {overall_average:.2f}")

import numpy as np

# Student grades data (randomly generated)
np.random.seed(42)
grades = np.random.randint(60, 100, size=(20, 4))
print("Student Grades Data:")
print(grades)

# Task 1: Average Grade for Each Student
average_grades = np.average(grades, axis=1)
print("\nTask 1: Average Grade for Each Student:")
print(average_grades)

# Task 2: Highest Grade in Each Subject
highest_grades = np.max(grades, axis=0)
print("\nTask 2: Highest Grade in Each Subject:")
print(highest_grades)

# Task 3: Students who have failed in at least one subject
failed_students = np.where(np.any(grades < 60, axis=1))[0]
print("\nTask 3: Students who have failed in at least one subject:")
print(failed_students)

# Task 4: Overall Average Grade for the Class
overall_average = np.mean(grades)
print("\nTask 4: Overall Average Grade for the Class:")
print(overall_average)
