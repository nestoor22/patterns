from functools import partial


class ImageBase(object):
    @classmethod
    def create(cls, width, height):
        return cls(width, height)

    def draw(self, x, y, color):
        raise NotImplementedError()

    def fill(self, color):
        raise NotImplementedError()

    def save(self, filename):
        raise NotImplementedError()


class Image(ImageBase):
    def __init__(self, width, height):
        self._width = int(width)
        self._height = int(height)

    def draw(self, x, y, color):
        print('Paint dot; coords: (%d, %d); color: %s' % (x, y, color))

    def fill(self, color):
        print('Fill color %s' % color)

    def save(self, filename):
        print('Save file as %s' % filename)


class ImageProxy(ImageBase):

    def __init__(self, *args, **kwargs):
        self._image = Image(*args, **kwargs)
        self.operations = []

    def draw(self, *args):
        func = partial(self._image.draw, *args)
        self.operations.append(func)

    def fill(self, *args):
        func = partial(self._image.fill, *args)
        self.operations.append(func)

    def save(self, filename):
        map(lambda f: f(), self.operations)
        self._image.save(filename)


if __name__ == '__main__':

    img = ImageProxy(200, 200)
    img.fill('gray')
    img.draw(0, 0, 'green')
    img.draw(0, 1, 'green')
    img.draw(1, 0, 'green')
    img.draw(1, 1, 'green')
    img.save('image.png')