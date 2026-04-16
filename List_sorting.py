
marks=[87,54,49,33,71,85,44]
print(sorted(marks))
print(marks)
print(sorted(marks,reverse=True))
# Original list of letters
alpha = ["k", "p", "a", "x"]

# Print the sorted version (ascending), without modifying the original list
sorted_alpha = sorted(alpha)
print("Sorted (ascending):", sorted_alpha)

# Reverse the original list in-place
alpha.reverse()
print("Reversed original list:", alpha)
