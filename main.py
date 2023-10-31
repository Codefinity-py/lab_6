# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.d
class Transport:
    # введіть # свій код тут
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power
    def accelerate(self, accelerateBy):
        self.speed += accelerateBy
    pass

class Car(Transport):
    def __init__(self, speed, power, fuel):
       super().__init__(speed, power)
       self.fuel = fuel
    def speed_plus(self):
        self.speed += 30

class Bicycle(Transport):
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals
    def speed_plus(self):
        self.speed += 10


BMW = Car(100, 150, 'Бензин')
print('До прискорення', BMW.speed)
BMW.speed_plus()
print('Після прискорення', BMW.speed)

my_bicycle = Bicycle(20, 5, 2)
print('До прискорення', my_bicycle.speed)
my_bicycle.speed_plus()
print('Після прискорення', my_bicycle.speed)
