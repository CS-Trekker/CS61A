class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    class_num = "205"
        
    def getolder(self, years):
        self.age += years
        print(f"{self.name} is now {self.age} years old.")
        

Tom = Student("Tom", 20)

print(type(Student), type(Tom))

print(Tom.age, Tom.class_num)

print(getattr(Tom, "name"))

print(hasattr(Tom, "sex"))

Student.getolder(Tom, 5)
print(type(Student.getolder))

Tom.getolder(5)
print(type(Tom.getolder))