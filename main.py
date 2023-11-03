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

    def accelerate(self, accelerate):
        self.speed += accelerate

    def __str__(self):
        return f"Speed: {self.speed}, Power: {self.power}"

class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel

    def __str__(self):
        return super().__str__() + f", Fuel: {self.fuel}"

class Bicycle(Transport):
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals

    def __str__(self):
        return super().__str__() + f", Number of pedals: {self.pedals}"

car = Car(150, 100, "Diesel")
bicycle = Bicycle(15, 5, 2)

print("Before speed up:")
print("Car: ", car)
print("Bicycle:", bicycle)

car.accelerate(20)
bicycle.accelerate(10)

print("After speed up:")
print("Car: ", car)
print("Bicycle: ", bicycle)
