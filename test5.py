class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(self.name, self.id)
#================================
class CSEStudent(Student):
    def __init__(self, name, id, no_labs):
        super().__init__(name, id)
        self.no_labs = no_labs
    def cry(self):
        print("cse students are crying due to", self.no_labs)
#==================================
class BBAStudent(Student):
    def party(self):
        print( "all day party")
#===================================
cs = CSEStudent("Bob", 11, 10)
ba = BBAStudent("carol", 33)
cs.details()
ba.details()
cs.cry()
ba.party()

