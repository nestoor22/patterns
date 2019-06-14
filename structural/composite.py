class Graphic(object):
    def draw(self):
        raise NotImplementedError()

    def add(self, obj):
        raise NotImplementedError()

    def remove(self, obj):
        raise NotImplementedError()

    def get_child(self, index):
        raise NotImplementedError()


class Line(Graphic):

    def draw(self):
        print('Лінія')


class Rectangle(Graphic):

    def draw(self):
        print('Прямокутник')


class Text(Graphic):
    def draw(self):
        print('Текст')


class Picture(Graphic):

    def __init__(self):
        self._children = []

    def draw(self):
        print('Картинка')
        # Викликає малювання вкладених об'єктів
        for obj in self._children:
            obj.draw()
        print('Намальовано')

    def add(self, obj):
        if isinstance(obj, Graphic) and not obj in self._children:
            self._children.append(obj)

    def remove(self, obj):
        index = self._children.index(obj)
        del self._children[index]

    def get_child(self, index):
        return self._children[index]

if __name__ == '__main__':
    pic = Picture()
    pic.add(Line())
    pic.add(Rectangle())
    pic.add(Text())
    pic.add(Line())
    pic.draw()
    print("PIC 2")
    pic2 = Picture()
    pic2.add(pic)
    pic2.add(Text())
    pic2.draw()
