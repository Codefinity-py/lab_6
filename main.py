# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport():
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def accelerate(self, additionalSpeed):
        self.speed += additionalSpeed

    def __repr__(self) -> str:
        return f"Speed = {self.speed}, Power = {self.power}"
      

class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel

    def __repr__(self) -> str:
        return "Car: " + super().__repr__() + f", Fuel = {self.fuel}"

class Bicycle(Transport):
    def __init__(self, speed, power, pedals = 2):
        super().__init__(speed, power)
        self.pedals = pedals


    def __repr__(self) -> str:
        return "Bicycle: " + super().__repr__() + f", Pedals = {self.pedals}"

car_1 = Car(100, 40, 100)
bicycle_1 = Bicycle(15, 15)

print(car_1.__repr__())
car_1.accelerate(45)
print(car_1.__repr__())

print(bicycle_1.__repr__())
bicycle_1.accelerate(15)
print(bicycle_1.__repr__())