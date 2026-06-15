class Person:
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept

p1 = Person('Mohammad','SWE')
p2 = Person('Naim','SWE')
p3 = Person('Qaseem','CSE')

L = [p1,p2,p3]

print(L) # print the memory address

for i in L :
    print(i.name,i.dept)


