class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(object, metaclass=Singleton):
    def __init__(self, color):
        self.color = color

if __name__ == '__main__':
    obj1 = MyClass('black')
    print(obj1.color) # Print 'black'
    obj2 = MyClass('red')
    print(obj2.color) # Print 'black'
    print(obj1 is obj2) # Print True
