#base class / parent class 

class Phone :
    category= "Electronics"

    #constructor

    def __init__(self,model,battery,camera,battery_percentage=100):
        self.model=model
        self.battery =battery
        self.camera =camera
        self.batter_percenatage = battery_percentage
     
   #methods
    def charge(self,hour):
        self.charge+=hour 

#creating object
apple = Phone("I_phone17",4500,50)
blueberry =Phone("Blue_berry_5",5000,40)
iqoo = Phone("z9_turbo",5000,50)

print(apple.batter_percenatage)
print(blueberry.camera)
print(iqoo.model)

#single inheritence
#child/derived clas
class SmartPhone(Phone) :
    def __init__(self, model, battery, camera,processor):
        super().__init__(model, battery, camera )
        self.processor = processor

pro=SmartPhone("X",5000,60,"snapdragon")
print(pro.model)

