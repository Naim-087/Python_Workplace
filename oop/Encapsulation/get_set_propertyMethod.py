class Student:
    def __init__(self):
        self.__name = "Naim"

    
        

    @property    # A getter to get name
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value

s = Student()

s.name= "Mohammad"
print(s.name)

