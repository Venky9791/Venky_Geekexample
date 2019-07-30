class Car:
    __name=""
    __maxspeed = 0


    def __init__(self):
        self.__updateSoftware()
        self.__name = "Supercar"
        self.__maxspeed=320


    def drive(self):
        print("Driving")
        print("name of the car  " + self.__name)


    def __updateSoftware(self):
        print("Updating Software")

    def sayHello(self,name=None):
        if name is None:
            print ("Hello")
        else:
            print("Hello" + name)


redcar = Car()
redcar.sayHello()
redcar.sayHello("Venky")
redcar.drive()
print(redcar._Car__maxspeed)
#redcar._Car__updateSoftware()
