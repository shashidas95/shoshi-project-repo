class Student:
    def __init__(self, name, Id):
        self.name = name #instance variable
        self.id = Id # instance variable
        print("object is created")

    def details(self):   # instance method
        print("Name: ", self.name, "ID: ",self.id)
#*************************************************

s1 = Student("shashi", "12345")
s2 = Student("robi", 1234)

s1.details()