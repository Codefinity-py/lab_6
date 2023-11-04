# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport:
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def accelerate(self, acceleration):
        self.speed += acceleration
        print(f"Speed increased to {self.speed} km/hour.")


class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel


class Bicycle(Transport):
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals


car1 = Car(speed=70, power=117, fuel='Diesel')
print(f'Car: Speed {car1.speed} km/hour, Power {car1.power}, Fuel {car1.fuel}')
car1.accelerate(17) 

bicycle = Bicycle(speed=27, power=117, pedals=2)
print(f'Bicycle: Speed {bicycle.speed} km/hour, Power {bicycle.power}, Pedals {bicycle.pedals}')
bicycle.accelerate(4) 

        
