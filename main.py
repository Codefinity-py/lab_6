# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport:
    # введіть свій код тут
    pass
    def __init__(self, power, speed):
        self.power = power
        self.speed = speed
    def accelerate(self, add_speed):
        self.speed += add_speed

class Car(Transport):
    def __init__(self, power, speed, fuel):
        super().__init__(power, speed)
        self.fuel = fuel

class Bicycle(Transport):
    def __init__(self, power, speed, pedals):
        super().__init__(power, speed)
        self.pedals = pedals

car = Car(200, 120, "бензин")
bike = Bicycle(25, 20, 2)

car.accelerate(15)
bike.accelerate(7)

print(f"Автомобіль: speed - {car.speed}, пальне - {car.fuel}")
print(f"Велосипед: speed - {bike.speed}, кількість педалей - {bike.pedals}")

