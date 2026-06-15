class Birds:
    def __init__(self,name):
         self.name = name

   

class Sparrow(Birds):
     def __init__(self, name,color):
          super().__init__(name)
          self.color = color

     def display(self):
          print("Name : ", self.name)
          print("Color : ", self.color)

b = Sparrow("Sparrow","Brown and Gray")

b.display()
