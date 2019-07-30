class Document:

    def __init__(self,name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement Abstract Method")


class Word(Document):

    def show(self):
        return "show Word Contents"

class PDF(Document):

    def show(self):
        return "Show PDF Contents"

documents = [PDF('Document1'),Word('Document2'),PDF('Document3')]

for document in documents:
    print("Document name {} ".format(document.name) + document.show())

