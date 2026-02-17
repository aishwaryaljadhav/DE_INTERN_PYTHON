class Car:
    @staticmethod
    def start_engine():
        print("Engine started")
    @staticmethod
    def stop_engine():
        print("Engine stopped")

class ElectricCar(Car):
    def __init__(self, name):
        self.name = name

class Tesla(ElectricCar):
    def __init__(self, type):
        self.type=type

car1 = ElectricCar("Tesla")
print(car1.name)
car1.start_engine()
car2 = Tesla("Model S")
print(car2.type)
car2.start_engine()