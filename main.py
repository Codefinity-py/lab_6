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

    def accelerate(self, speed_increase):
        self.speed += speed_increase


class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel


class Bicycle(Transport):
    def __init__(self, speed, power, number_of_pedals):
        super().__init__(speed, power)
        self.number_of_pedals = number_of_pedals


passat = Car(210, 250, 'Diesel')
cube = Bicycle(20, 5, 2)

passat.accelerate(50)
cube.accelerate(10)

print(f"Car speed: {passat.speed} km/h")
print(f"Bicycle speed: {cube.speed} km/h")
pass