
def Reverse(tuples):
    new_tup = tuples[::-1]
    return  new_tup

def Reversed(tuples):
    new_tup = ()
    for k in reversed(tuples):
        new_tup = new_tup + (k,)
    print(new_tup)

tuples = (10,20,30,40,50)
Reversed(tuples)


tup1 = (['a', 'apple'], ['b', 'ball'])

for first,second  in  tup1:
    print (first)
    print(second)
    print("*" ,10)