class Student:
    def __init__(self,name,dob,d1,d2,d3):
        self.name = name 
        self.dob = dob
        self.total = d1 + d2 + d3
    
    def __str__(self):
        return self.name+" "+self.dob+" "+'{:.1f}'.format(self.total)
    
print(Student(input(), input(), float(input()), float(input()), float(input())))
        