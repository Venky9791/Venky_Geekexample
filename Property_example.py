class Celsius:
    def __init__(self,temperature=0):
        self._temperature = temperature

    # def get_temperature(self):
    #     print("Getting Value")
    #     return self._temperature
    #
    # def set_temperature(self,temperature):
    #     print("Setting Value")
    #     if temperature < -273:
    #         raise ValueError("Temperature below -273 is not Possible")
    #     self._temperature = temperature

    @property
    def temperature(self):
        print("Getting Value")
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        print("Setting Value")
        if temperature < -273:
            raise ValueError("Temperature below -273 is not Possible")
        self._temperature = temperature


    def to_farenheit(self):
        return (self.temperature * 1.8) + 32

   # temperature = property(get_temperature,set_temperature)

man = Celsius()
man.temperature=37
#man.set_temperature(-300)
print(man.to_farenheit())
#print(man.__dict__)
#print(man.__class__)
#print(man.__doc__)
#print(man.__dir__())
