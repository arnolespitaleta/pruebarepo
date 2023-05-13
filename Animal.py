class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class CatDog(Dog, Cat):
    pass

my_pet = CatDog("Fido")
print(my_pet.speak())