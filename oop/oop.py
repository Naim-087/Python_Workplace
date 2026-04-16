#creating class and object

class Student :
    def __init__(self,name,id,gpa,result) :
        self.name=name
        self.id =id
        self.gpa=gpa
        self.result= result

    


student1 = Student("Naim Islam",101,3.85,"passed")
student2 = Student("Ahmed ali",201,3.6,"passed")
student3 = Student("iqkram khan",105,3.71,"passed")
print("Name :",student1.name,"ID:",student1.id,"GPA:",student1.gpa,"Result:",student1.result)
print("Name :",student2.name,"ID:",student2.id,"GPA:",student2.gpa,"Result:",student2.result)
print("Name :",student3.name,"ID:",student3.id,"GPA:",student3.gpa,"Result:",student3.result)