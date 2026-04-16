# Armstrong Number Checker

num = int(input("Enter a number: "))

# Find the number of digits
order = len(str(num))

# Initialize sum
sum = 0

# Make a copy of the number
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

# Check if the number is an Armstrong number
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
