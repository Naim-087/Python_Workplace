users = ["Alice", "", "Bob", None, "Charlie"]

# In Python, empty strings and None are 'False'
# Putting None as the function tells filter to remove all 'False' items
clean_users = filter(None, users)

print(list(clean_users)) # ['Alice', 'Bob', 'Charlie']