from datetime import date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age >=18


Person1 = Person("Venky",21)
Person2 = Person.fromBirthYear("Venky",1996)

print(Person1.age)
print(Person2.age)
print(Person2.isAdult(22))


