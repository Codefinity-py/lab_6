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
    def quickening(self, speed_up):
      self.speed += speed_up

class Car:
   def __init__(self, speed, power, fuel): 
      self.fuel = fuel

class Bike:
   def __init__(self, speed, power, pedali):
      self.pedali = pedali

BMV = Car(100, 150, 'Соляра')
BMX = Bike(15, 20, 2)

BMV.quickening(10)
BMX.quickening(3)

print(f"Car: spead = {BMV.speed}, fuel = {BMV.fuel}")
print(f"Bike: spead = {BMX.speed}, pedali = {BMX.pedali}")
