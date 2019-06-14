class Man(object):
    def __init__(self, name):
        self._name = name

    def say(self):
        print ('Hi! My name is %s!' % self._name)


class Jetpack(object):

    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def fly(self):
        print ('%s fly with jetpack!' % self._man._name)


if __name__ == '__main__':
    man = Man('Mark')

    man_jetpack = Jetpack(man)
    man_jetpack.say()
    man_jetpack.fly()