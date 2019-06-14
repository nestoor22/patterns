import weakref


class Type(object):

    def __init__(self, type):
        self._type = type

    def __str__(self):
        return self._type


class TypeFactory(object):
    _types = weakref.WeakValueDictionary()

    @classmethod
    def get_types(cls, name):
        value = cls._types.get(name)
        if value is None:
            value = Type(name)
            cls._types[name] = value
        return value


class PlaceMarket(object):

    def __init__(self, x, y, type_name):
        self._x = x
        self._y = y
        self._type = TypeFactory.get_types(type_name)

    def __str__(self):
        args = (self._type, self._x, self._y,)
        return "Color: %s, Position: %.3f, %.3f" % args


if __name__ == '__main__':

    tree1 = PlaceMarket(-45.1245221, 64.4352123, 'larch')
    tree2 = PlaceMarket(34.2123123, 43.455555, 'larch')

    print(tree1._type is tree2._type)
    print(tree1)
    print(tree2)

