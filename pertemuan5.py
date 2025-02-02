from abc import ABC, abstractclassmethod

class Animal(ABC):
    def speak(self):
        pass
    def foot(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"
    def foot(self):
        return 4
    
class Chicken(Animal):
    def speak(self):
        return "Chick-Chick!"
    def foot(self):
        return 2
    
    
#abstract
def animal_behavior(animal: Animal):
    print(f"The animal says: {animal.speak()}")
    print(f"The animal has: " + str(animal.foot()) + " legs")
    
dog = Dog()
chicken = Chicken()

animal_behavior(dog);
animal_behavior(chicken);
# print("Sound of the dog :", dog.speak(), " Dog has :", dog.foot(), " foot")