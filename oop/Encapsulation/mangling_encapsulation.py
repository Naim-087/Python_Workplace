class Employee:

    def __init__(self):
        self.__id = 1003

e = Employee()

e._Employee__id = 4000

print(e._Employee__id)