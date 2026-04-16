import pandas as pd
# test_pandas.py


# Create a simple DataFrame
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "GPA": [3.5, 3.7, 3.2, 3.9, 3.8]
}

df = pd.DataFrame(data)

# Print the whole DataFrame
print("Full DataFrame:")
print(df)

# Print the first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# Print summary statistics
print("\nSummary statistics:")
print(df.describe())

# Filter rows where GPA > 3.5
high_gpa = df[df["GPA"] > 3.5]
print("\nStudents with GPA > 3.5:")
print(high_gpa)
