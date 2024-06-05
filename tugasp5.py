from abc import ABC, abstractclassmethod

class Car(ABC):
    def fasilitas(self):
        pass
    def kecepatan(self):
        pass
    def harga(self):
        pass
    def kekuatan(self):
        pass

class BMW(Car):
    def fasilitas(self):
        return "Performance Center"
    def kecepatan(self):
        return 235 - 250
    def harga(self):
        return "1,25M - 1,44M"
    def kekuatan(self):
        return "Performa yang Unggul"
    
class Avanza(Car):
    def fasilitas(self):
        return "Ruangan Luas dan Fleksibel"
    def kecepatan(self):
        return 160 - 180
    def harga(self):
        return "200jt"
    def kekuatan(self):
        return "Daya Tahan dan Handal"
    
class Ferrari(Car):
    def fasilitas(self):
        return "Desain yang iconic"
    def kecepatan(self):
        return 320 - 340
    def harga(self):
        return "$200,000 - $250,000"
    def kekuatan(self):
        return "Performa Luar Biasa"
    
    
#abstract
def car_behavior(car: Car):
    print(f"Fasilitas: {car.fasilitas()}")
    print(f"Kecepatan: " + str(car.kecepatan()) + " legs")
    print(f"Harga: {car.harga()}")
    print(f"Kekuatan: {car.kekuatan()}")
    
bmw = BMW()
avanza = Avanza()
ferrari = Ferrari()

car_behavior(bmw);
print()
car_behavior(avanza);
print()
car_behavior(ferrari);
