class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name, "is eating")
#=======================================
class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")
#=====================================
a1 = Animal("jack")
d1 = Dog("rover")
# a1.eat()
# d1.bark()
# d1.eat()
print(isinstance(a1, Animal))
print(isinstance(d1, Dog))
print(issubclass(Dog, Animal))