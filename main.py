# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport():
    # введіть свій код тут
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def accelerate(self, additionalSpeed):
        self.speed += additionalSpeed

    def __str__(self) -> str:
        return f"Transport Speed = {self.speed}, Transport Power = {self.power}"


class Car(Transport):
    def __init__(self, speed, power, diesel):
        super().__init__(speed, power)
        self.diesel = diesel

    def __str__(self) -> str:
        return super().__str__() + f", Transport Diesel = {self.diesel}"


class Bike(Transport):
    def __init__(self, speed, power, pedals=2):
        super().__init__(speed, power)
        self.pedals = pedals

    def __str__(self) -> str:
        return super().__str__() + f", Transport Pedals = {self.pedals}"


car = Car(130, 90, 70)
bike = Bike(20, 10)

print("Car")
print(car.__str__())
print("Accelerating: vroom vroom")
car.accelerate(50)
print(car.__str__())
print("\n")

print("Bike")
print(bike.__str__())
print("Accelerating: vroom")
bike.accelerate(10)
print(bike.__str__())
print("\n")

