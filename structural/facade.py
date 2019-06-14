class Car(object):

    def __init__(self, consumption):
        self._consumption = consumption

    def get_consumption(self):
        return self._consumption

    def start(self, tank):
        tank.ride(self._consumption)


class Tank(object):
    def __init__(self, fuel):
        self._fuel = fuel

    def ride(self, consumption):
        if self._fuel > consumption:
            print("Can ride more than 100 km")
            self._fuel -= consumption
            return True

        elif 0 < self._fuel <= consumption:
            print("Can ride %.2f km" % ((self._fuel/consumption) * 100))
            self._fuel -= consumption
            return True

        else:
            print("Fuel low")
            return False


class Facade(object):

    def __init__(self):
        self.car = Car(27)
        self.tank = Tank(50)

    def go(self):
        return self.car.start(self.tank)


if __name__ == '__main__':
    f = Facade()
    f.go()  # Can ride more than 100 km
    f.go()  # Can ride 85.19 km
    f.go()  # Fuel low

