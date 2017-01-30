class Car:

class Taxi(Car):
    """ specialised version of a Car that includes fare costs """
    price_per_km = 1.2

    def __init__(self, name, fuel, price_per_km):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        Taxi.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
@@ -59,3 +60,19 @@ class Taxi(Car):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

class UnreliableCar(Car):
    def __init__(self, fuel, reliability):
        super().__init__("Unreliable car", fuel)
        self.reliability = reliability

    def drive(self, distance):
        from random import randint
        rand_no = randint(0, 100)
        if rand_no < self.reliability:
            super().drive(distance)

lousy_car = UnreliableCar(100, 50)
print(lousy_car)
lousy_car.drive(50)
print(lousy_car)