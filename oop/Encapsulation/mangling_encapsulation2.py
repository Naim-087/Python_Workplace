class employee:
    def __init__(self):
        self.__id = 1011
        self.__name = "Naim"    
        self.__salary = 40000


e= employee()
e._employee__salary=80000 # accessing private var without getter and setter

print(e._employee__salary)
