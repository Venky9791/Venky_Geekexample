class Account:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print ("Account Created for {}".format(self.name))


    def deposit(self,amount):
        if amount > 0 :
            newbal = self.balance+ amount
            print("Your current Balance {} and Balance After Deposit {}".format(self.balance,newbal))


    def withdrawl(self, amount):
        if amount < 0 or amount > self.balance:
            print ("The With drawl Amount should be more than 0 and less than your current balance {}".format(self.balance))
        else:
            self.balance = self.balance - amount
            print ("Balance after withdrawl {}".format (self.balance))

    def show_Balance(self):
        print ("Cureent Balance {}".format(self.balance))




if __name__ == '__main__':
     tim = Account("Venky",0)
     tim.show_Balance()

     tim.deposit(2000)
     tim.withdrawl(2000)



