class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

    def park(self):
        if self.mode == "driving":
            self.mode = "parking"
            self.speed = 0
            print("Parked my", self.bodystyle)
        else:
            print(self.bodystyle, "is already parked")


class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", speed)


class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype


car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)

car1.park()
car2.park()
car1.park()
mc1.park()
mc1.park()
