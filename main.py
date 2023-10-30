# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.


class Transport():
    speed = 0
    power = 0
    def accelerate(self, strength):
        self.speed+=strength

    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

class Car(Transport):
    fuel = ''
    def __init__(self,speed,power,fuel):
        super().__init__(speed, power)
        self.fuel = fuel

class Bicycle(Transport):
    pedals = ''
    def __init__(self,speed,power,pedals):
        super().__init__(speed, power)
        self.pedals = pedals

auto1 = Car(10,5,'diesel')
auto1.accelerate(5)
cycle1 = Bicycle(1,5,2)
auto1.accelerate(1)
