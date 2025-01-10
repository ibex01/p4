import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Subject1": [85, 45, 70, 30, 90],
    "Subject2": [75, 55, 80, 40, 85],
    "Subject3": [95, 65, 60, 35, 95],
    "Subject4": [80, 50, 75, 20, 88],
    "Subject5": [90, 60, 65, 50, 92],
}

df = pd.DataFrame(data)

# a) Calculate the total marks for each student
df["Total Marks"] = df.iloc[:, 1:].sum(axis=1)

# b) Filter out students who scored less than 50% overall
passing_marks = 250  # 50% of 500
passed_students = df[df["Total Marks"] >= passing_marks]

# c) Display the names and scores of passed students
print("Students who passed (50% or more):")
print(passed_students[["Name", "Total Marks"]])

# d) Filter out students who scored less than 50%
failed_students = df[df["Total Marks"] < passing_marks]
print("\nStudents who scored less than 50%:")
print(failed_students[["Name", "Total Marks"]])
