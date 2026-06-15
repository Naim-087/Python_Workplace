class Birds:
    def eat(self):
        print("Eating")

class sparrow(Birds):
    def fly(self):
        print("Flying")

S =sparrow()
S.eat()
S.fly()