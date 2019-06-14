class HttpHandler(object):

    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(HttpHandler):

    def handle(self, code):
        if code == 404:
            return 'Сторінка не знайдена'


class Http500Handler(HttpHandler):

    def handle(self, code):
        if code == 500:
            return 'Помилка сервера'


class Client(object):
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print('Помилка: %s' % msg)
                break
        else:
            print('Невідомий код помилки')


client = Client()
client.add_handler(Http404Handler())
client.add_handler(Http500Handler())
client.response(400)
client.response(404)
client.response(500)