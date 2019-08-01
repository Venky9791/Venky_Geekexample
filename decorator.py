def succ(x):
    print(x*x)

succ(10)

succssor = succ

succssor(5)

del succ

succssor(15)
#succ(3)

#
# def f():
#
#
#     def ga():
#         print("Hi i am in G")
#
#     print("I am in f")
#     ga()
#
# f()


def temperature(t):
    def celsius2farenheit(x):
        return 9 * x / 5+ 32
    result = "Its " + str(celsius2farenheit(t)) + "Degress"
    return result

print(temperature(20))


def g():
    print("Hi This is me G")

def f(func):
    print("This is me F")
    print("Let me call func")
    func()
    print("Function Real name is " +  func.__name__)
f(g)

