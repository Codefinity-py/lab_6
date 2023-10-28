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
    
    def accelerate(self, add_speed):
        self.speed += add_speed


class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel

    def accelerate(self, add_speed):
        super().accelerate(add_speed)
        print(f"Acceleration for Car: {self.speed}")


class Bicycle(Transport):
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals

    def accelerate(self, add_speed):
        super().accelerate(add_speed)
        print(f"Acceleration for Bicycle: {self.speed}")


car1 = Car(130, 400, "Petrol")
bicycle1 = Bicycle(10, 1, 2)

car1.accelerate(30)
bicycle1.accelerate(5)

