import copy


class Prototype(object):

    def __init__(self):
        self.objects = {}

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name):
        del self.objects[name]

    def clone(self, name, attrs):
        new_obj = copy.deepcopy(self.objects[name])
        new_obj.__dict__.update(attrs)
        return new_obj


class Car(object):
    pass

if __name__ == '__main__':
    prototype = Prototype()
    prototype.register('car', Car())

    bmw = prototype.clone('car', {'name': 'BMW', 'doors': 4})
    print(bmw.name, bmw.doors)
