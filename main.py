# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

# from abc import ABC, abstractclassmethod


class Transport():
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power
    
    def accelerate(self, additionalSpeed):
        self.speed += additionalSpeed

    def __str__(self) -> str:
        return f"Transport Speed = {self.speed}, Power = {self.power}"        

class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel

    def __str__(self) -> str:
        return super().__str__() + f", Fuel = {self.fuel}"

class Bicycle(Transport):
    def __init__(self, speed, power, pedals = 2):
        super().__init__(speed, power)
        self.pedals = pedals

        
    def __str__(self) -> str:
        return super().__str__() + f", Pedals = {self.pedals}"

car_1 = Car(60, 20, 100)
bicycle_1 = Bicycle(5, 5)

print("Car:")
print(car_1.__str__())
print("Accelerating~~~~~~~~~~")
car_1.accelerate(30)
print(car_1.__str__())
print("\n")

print("Bicycle:")
print(bicycle_1.__str__())
print("Accelerating~~~~~~~~~~")
bicycle_1.accelerate(10)
print(bicycle_1.__str__())
print("\n")

