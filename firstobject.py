class kettle(object):

    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = kettle("Kenwood",12.99)
kenwood.price = 15.99

kenwood.power = 1.5

Bosch = kettle ("Bosch",10)

print (kenwood.make,kenwood.price)
print (Bosch.make,Bosch.price)

print ("Model {} and Price is {}".format(kenwood.make,kenwood.price))
print ("Model {0.make} and Price is {0.price} Swtch status {0.on}".format(Bosch))
Bosch.switch_on()
kettle.switch_on(kenwood)
print(kenwood.on)
print((kenwood.power))

