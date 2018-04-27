import abc

class Car:
    cars_in_fleet = 0

    def __init__(self, year, km_per_liter):
        """ Car """
        self.year = year

    # Static methods are useful when we don't need information about each object
    @staticmethod
    def alcohol_or_gas(gas_price, alcohol_price):
        """ Which is best? """
        if gas_price * 0.7 > alcohol_price:
            print("Use alcohol")
        else:
            print("Use gas")

    # Class methods are usefull when we need to change properties of the class
    # itself, that don't depend on the object
    @classmethod
    def add_car_to_fleet(cls):
        cls.cars_in_fleet += 1

tel = Car(2018, 12)
tel.add_car_to_fleet()
tel.alcohol_or_gas(4, 3)
print("Number of cars in fleet: {}".format(Car.cars_in_fleet))
