def fib(limit):
    a,b = 0,1

    while a < limit:
        print("Before Yield {}".format(a))
        yield a
        print("After Yield {}".format(a))
        a,b = b,a+b

x = fib(5)

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

#for i in fib(5):
 #   print(i)

