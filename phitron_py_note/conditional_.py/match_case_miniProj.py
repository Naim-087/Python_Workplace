print('''
___User Login System___
''')

# Step 1: Input
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
role = input("Enter role (admin/user/guest): ").strip().lower()

# Step 2: Username validation
if username == "":
    print("Username cannot be empty")

elif " " in username:
    print("Username must not contain spaces")

# Step 3: Password validation
elif password == "":
    print("Password cannot be empty")

elif len(password) < 8:
    print("Password must be at least 8 characters")

# no uppercase
elif password == password.lower():
    print("Password must contain at least 1 uppercase letter")

# no lowercase
elif password == password.upper():
    print("Password must contain at least 1 lowercase letter")

elif password == username:
    print("Password must not be same as username")

elif " " in password:
    print("Password must not contain spaces")

elif not password[0].isalnum():
    print("Password must start with a letter or digit")

elif not password[-1].isalnum():
    print("Password must end with a letter or digit")

# Step 4: Role check using match-case
else:
    print("\nLogin Successful ✅")

    match role:
        case "admin":
            print("Access Level: Full Access 🔥")
        case "user":
            print("Access Level: Limited Access")
        case "guest":
            print("Access Level: Read Only")
        case _:
            print("Unknown Role ❌")
