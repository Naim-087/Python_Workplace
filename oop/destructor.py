class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        print(f"Student {self.name} created.")

    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.student_id)

    def __del__(self):
        print(f"Student {self.name} deleted.")


# Creating object
s1 = Student("Naim", 221)

# Displaying information
s1.display_info()

# Deleting object
del s1