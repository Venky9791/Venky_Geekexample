class Car(object):
    def factory (type):
        if type == "Racecar":
            return Racecar()
        elif type == "Van":
            return Van()

    factory = staticmethod(factory)


class Racecar(Car):

    def drive(self):
            print("Race Car Driving")

class Van(Car):

    def drive(self):
            print("Race Car Driving")

obj= Car.factory("Racecar")
obj.drive()
