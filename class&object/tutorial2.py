# Creating classes
class Vehicle():
    def __init__(self, price, gas, color) -> None:
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed) -> None:
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print("Beep beep")


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires) -> None:
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print("Honk honk")
