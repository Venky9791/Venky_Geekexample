
class Human:

    name = ""
    def __init__(self,name):
        self.name = name
        self.Head = self.Head()


    class Head:

        def talk(self):
            return "Talking"


def Main():
    Person1 = Human("Venky")
    print(Person1.Head.talk())


if __name__ == '__main__':
    Main()

