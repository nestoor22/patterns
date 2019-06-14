class Builder(object):

    def build_body(self):
        raise NotImplementedError()

    def build_engine(self):
        raise NotImplementedError()

    def build_fuel_tank(self):
        raise NotImplementedError()


class Car(object):

    def __init__(self, body, engine, fuel_tank):
        self._start = False
        self._body = body
        self._engine = engine
        self._fuel_tank = fuel_tank

    def start(self):
        self._start = True

    def off(self):
        self._start = False

    def __str__(self):
        return "COLOR: {0}".format(self._body._color)


class Body(object):

    def __init__(self, counts_of_doors, color):
        self._doors = counts_of_doors
        self._color = color


class Engine(object):

    def __init__(self, power):
        self._power = power


class FuelTank(object):

    def __init__(self, capacity):
        self._capacity = capacity


class CarBuilder(Builder):

    def build_body(self):
        return Body(4, 'black')

    def build_engine(self):
        return Engine(232)

    def build_fuel_tank(self):
        return FuelTank(80)

    def create_car(self):
        body = self.build_body()
        engine = self.build_engine()
        fuel_tank = self.build_fuel_tank()
        return Car(body, engine, fuel_tank)


if __name__ == '__main__':

    car_builder = CarBuilder()
    car = car_builder.create_car()
    car.start()
    print(car)




