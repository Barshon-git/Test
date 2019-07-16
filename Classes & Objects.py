class Student:

    def __init__(self,name,major,gpa,is_on_probation):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation= is_on_probation

student1=Student("Barshon","CSE",3.7, False)
student2=Student("Shoily","Endlish",4.0, True)
print(student1.gpa)
print(student2.gpa)