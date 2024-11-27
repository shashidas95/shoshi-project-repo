class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(self.name, self.id)
#================================
class CSEStudent(Student):
    def __init__(self, name, id, labs):
        super().__init__(name, id)
        self.labs =labs
    def cry(self):
        print("cse student", self.name, "is crying due to ", self.labs, "labs")
#==================================
class CSEFresher(CSEStudent):
    def enroll_cse101(self):
        print(self.name , "is enrolled course cse101" )
#==================================
obj1 = CSEStudent("bob", 33, 3)
obj2 = CSEFresher("carol", 44, 4)
obj1.details()
obj2.details()
obj1.cry()
obj2.cry()

