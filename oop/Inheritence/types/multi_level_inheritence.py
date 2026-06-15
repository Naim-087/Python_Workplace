class Person:
    def introduce(self):
        print("I am a man of Regular")

class Student(Person):
    def study(self):
        print("I am a undergraduate ")

class PHD(Student):
    def Got(self):
        print("After few Years I got a full funded PHD Offer")

P = PHD()
P.introduce()
P.study()
P.Got()