# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport:
    # введіть свій код тут
    def __init__(self, speed, power):
        self.speed = speed 
        self.power = power

    def accelerate(self, amount):   
        self.speed += amount 


class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel 


class Bicycle(Transport):     
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals


car = Car(100, 200, "gasoline") 
bicycle = Bicycle(20, 50, 2)      

car.accelerate(30)
bicycle.accelerate(10)


import unittest
from main import Transport, Car, Bicycle

class TestTransportMethods(unittest.TestCase):

    def test_accelerate(self):
        car = Car(100, 200, "gasoline")
        bicycle = Bicycle(20,50, 2)

        car.accelerate(30)
        bicycle.accelerate(10)

        self.assertEqual(car.speed, 130)
        self.assertEqual(bicycle.speed, 30)

if __name__ == ' __main__ ':
    unittest.main()        