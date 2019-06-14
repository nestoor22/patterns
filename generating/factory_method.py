
class Document(object):
    def show(self):
        raise NotImplementedError()


class ODFDocument(Document):
    def show(self):
        print('Open document format')


class MSOfficeDocument(Document):
    def show(self):
        print('MS Office document format')


class Application(object):
    def create_document(self, type_):
        raise NotImplementedError()


class MyApplication(Application):
    def create_document(self, type_):
        if type_ == 'odf':
            return ODFDocument()
        elif type_ == 'doc':
            return MSOfficeDocument()


if __name__ == '__main__':
    app = MyApplication()
    app.create_document('odf').show()
    app.create_document('doc').show()