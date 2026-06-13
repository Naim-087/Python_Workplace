class employee:
    def __init__(self):
        self.__id= 1003
        self.__name= "ABCD"
        self.__dept = "Software"

    def set_id(self,id):
        self.__id=id
       
    def get_id(self):
        return self.__id
    
e = employee()

e.set_id(2002)

print(e.get_id())