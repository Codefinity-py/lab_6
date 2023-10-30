# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class vehicle:
   def __init__(self, speed, power):
      self.speed = speed
      self.power = power
   def speed_up(self, speed_up):
      self.speed_up += speed_up

class car(vehicle):
   def __init__(self, speed, power, fuel): 
      self.speed = speed
      self.power = power
      self.fuel = fuel
   
   def speed_up(self, speed_up):
      self.speed_up += speed_up

class bike(vehicle):
   def __init__(self, speed, power, pedals):
      self.speed = speed
      self.power = power  
      self.pedals = pedals
   
   def speed_up(self, speed_up):
      self.speed_up += speed_up
   pass
