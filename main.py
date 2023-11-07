# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport:
    # введіть свій код тут
     pass
     def __init__(self, speed, power):
         self.speed = speed
         self.power = power
     def accelerate(self, add_speed=0):
         self.speed = max(self.speed + add_speed, 0)
     def __str__(self):
        return f'Speed: {self.speed}, Power: {self.power}'
class Car(Transport):
    def __init__(self, speed, power, fuel):
        self.speed = speed
        self.power = power
        self.fuel = fuel
    def __str__(self):
        return f'Speed: {self.speed}, Power: {self.power}, Fuel: {self.fuel}'
class Bicycle(Transport):
    def __init__(self, speed, power, pedals):
        self.speed = speed
        self.power = power
        self.pedals = pedals
    def __str__(self):
        return f'Speed: {self.speed}, Power: {self.power}, Number of pedals: {self.pedals}'

speed_car = 100
power_car = 130
fuel_car = 'Benz'

car = Car(speed_car, power_car, fuel_car)
car.accelerate(200)
print(car)

speed_bike = 25
power_bike = 10
pedals_bike = 2

bike = Bicycle(speed_bike, power_bike, pedals_bike)
bike.accelerate(30)
print(bike)




