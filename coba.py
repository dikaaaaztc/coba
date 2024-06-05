from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def facilities(self):
        pass
    
    @abstractmethod
    def speed(self):
        pass
    
    @abstractmethod
    def price(self):
        pass
    
    @abstractmethod
    def power(self):
        pass

class BMW(Car):
    def facilities(self):
        return "Luxury features"
    
    def speed(self):
        return "High speed"
    
    def price(self):
        return "Expensive"
    
    def power(self):
        return "High horsepower"

class Avanza(Car):
    def facilities(self):
        return "Basic features"
    
    def speed(self):
        return "Moderate speed"
    
    def price(self):
        return "Affordable"
    
    def power(self):
        return "Low horsepower"

class Ferrari(Car):
    def facilities(self):
        return "Luxury features"
    
    def speed(self):
        return "Extreme high speed"
    
    def price(self):
        return "Very expensive"
    
    def power(self):
        return "Very high horsepower"

# Abstract
def car_information(car: Car):
    print(f"Facilities: {car.facilities()}")
    print(f"Speed: {car.speed()}")
    print(f"Price: {car.price()}")
    print(f"Power: {car.power()}")

bmw = BMW()
avanza = Avanza()
ferrari = Ferrari()

car_information(bmw)
print()
car_information(avanza)
print()
car_information(ferrari)
