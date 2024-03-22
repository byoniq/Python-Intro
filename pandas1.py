import pandas as pd

data = [
    {'Name': 'John', 'Age': 25, 'Gender': 'Male', 'Occupation': 'Engineer', 'Salary': 60000},
    {'Name': 'Emily', 'Age': 30, 'Gender': 'Female', 'Occupation': 'Doctor', 'Salary': 90000},
    {'Name': 'Michael', 'Age': 35, 'Gender': 'Male', 'Occupation': 'Data Scientist', 'Salary': 80000},
    {'Name': 'Jessica', 'Age': 28, 'Gender': 'Female', 'Occupation': 'Teacher', 'Salary': 50000},
    {'Name': 'David', 'Age': 40, 'Gender': 'Male', 'Occupation': 'Manager', 'Salary': 100000},
    {'Name': 'Sarah', 'Age': 32, 'Gender': 'Female', 'Occupation': 'Software Developer', 'Salary': 75000},
    {'Name': 'Daniel', 'Age': 45, 'Gender': 'Male', 'Occupation': 'Consultant', 'Salary': 85000},
    {'Name': 'Rachel', 'Age': 27, 'Gender': 'Female', 'Occupation': 'Designer', 'Salary': 55000},
    {'Name': 'Chris', 'Age': 29, 'Gender': 'Male', 'Occupation': 'Marketing Specialist', 'Salary': 65000},
    {'Name': 'Laura', 'Age': 33, 'Gender': 'Female', 'Occupation': 'Accountant', 'Salary': 70000}
]

df = pd.DataFrame(data)

print(df.iloc[:,:1:] )


# df.to_excel('data.xlsx', index=False, sheet_name='Sheet1')

# # Print names
# print("Names:")
# print(df['Name'])

# # Print ages
# print("\nAges:")
# print(df['Age'])

# # Print gender
# print("\nGender:")
# print(df['Gender'])

# # Print occupation
# print("\nOccupation:")
# print(df['Occupation'])

# # Print salary
# print("\nSalary:")
# print(df['Salary'])

#Print ilocs 

print(df.iloc[:,:1:] )
