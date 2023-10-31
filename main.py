# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед", +
# які успадковують властивості та методи батьківського класу. +
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", + а також метод "прискорити", ===
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport:
    # введіть свій код тут
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def accelerate(self, add_speed=0):
        self.speed = max(self.speed + add_speed, 0)

    def __str__(self):
        return f'Speed: {self.speed}, Power: {self.power}'

class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel

    def __str__(self):
        return super().__str__() + f', Fuel: {self.fuel}'

class Bicycle(Transport):
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals

    def __str__(self):
        return super().__str__() + f', Number of pedals: {self.pedals}'

# дані для створення об'єкта Car
speed_Car = 100
power_Car = 150
fuel_Car = 'Diesel'

car = Car(speed_Car, power_Car, fuel_Car)
car.accelerate(240)
print(car)

# дані для створення об'єкта Bicycle
speed_Bike = 15
power_Bike = 5
pedals_Bike = 2

bike = Bicycle(speed_Bike, power_Bike, pedals_Bike)
bike.accelerate(20)
print(bike)