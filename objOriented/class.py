# -*- coding: utf-8 -*-
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print "To drive %d, it takes %.1f hours." % (distance, distance / self.speed)


class Bike(Vehicle):
    pass


class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print "need %.1f fuel" % (distance * self.fuel)

b = Bike(15)
c = Car(80, 0.012)
b.drive(100)
c.drive(100)
