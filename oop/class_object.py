class Car:
    def __init__(self,brand,color,body,engine):
         self.brand = brand
         self.color = color
         self.body = body
         self.engine = engine

car1 = Car("Toyota","White","Sedan","V6")
car2 = Car("Mercedez","Black","Hatchbacks","AMG V8s")

print(car1.brand ," ",car1.color, " ",car1.body, " ",car1.engine)
print(car2.brand ," ",car2.color, " ",car2.body, " ",car2.engine)



