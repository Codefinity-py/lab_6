# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Vehicle:
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power
    
    def accelerate(self, increment):
        self.speed += increment
        
class Car(Vehicle):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel
        
class Bicycle(Vehicle):
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals

car = Car(60, 150, "Gasoline") 
bicycle = Bicycle(15, 50, 2)

car.accelerate(15)
bicycle.accelerate(5)

print(f"Car speed:{car.speed} km/h")
print(f"Bicycle speed:{bicycle.speed} km/h")

    

