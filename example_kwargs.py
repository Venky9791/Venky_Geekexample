def myfun(*argv):
    for arg in argv:
        print(arg)


def myfun1(arg1,*argv):
    print("First Argument" + arg1)
    for arg in argv:
        print("Next Argeument" + arg)


def myfun2(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" %(key,value))

def myfun3(arg1,arg2,arg3):
    print("Arg1 " + arg1)
    print("Arg2 " + arg2)
    print("Arg3 " + arg3)


myfun('Hello','This','Is','Geeks')
myfun1('Hello','This','Is','Geeks')
myfun2(Name='Apple',Color='Red',Shape='Round')
args = ("Geeks", "for", "Geeks")
myfun3(*args)

kwargs = {"arg1" : "Geeks","arg2":"For","arg3":"Geeks"}

myfun3(**kwargs)