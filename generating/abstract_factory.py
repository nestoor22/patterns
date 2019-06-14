
class AbstractFactory:

    def create_auto(self):
        raise NotImplementedError()

    def create_plane(self):
        raise NotImplementedError()


class Auto:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Plane:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class ConcreteFactory1(AbstractFactory):

    def create_auto(self):
        return Auto('BMW')

    def create_plane(self):
        return Plane('AN-127')


if __name__ == '__main__':
    factory = ConcreteFactory1()
    print(factory.create_auto())
