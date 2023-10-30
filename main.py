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
   def acceleration(self, speed_up):
      self.speed += speed_up

class Car(Vehicle):
   def __init__(self, speed, power, fuel): 
      super().__init__(speed, power)
      self.fuel = fuel

class Bike(Vehicle):
   def __init__(self, speed, power, pedals):
      super().__init__(speed, power)
      self.pedals = pedals
   
car1 = Car(90, 200, 'дизель')
bike1 = Bike(20, 30, 2)

car1.acceleration(20)
bike1.acceleration(5)

print(f"Car: spead = {car1.speed}, fuel = {car1.fuel}")
print(f"Bike: spead = {bike1.speed}, pedals = {bike1.pedals}")
