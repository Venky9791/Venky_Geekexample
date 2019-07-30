tup1 = ();
print(tup1)

tup1 = ('Venky','Rani')
print(tup1)

list=[1,2,3,4,5]
tup1 = tuple(list)
print(list)
print(tup1)

tup1 = ('Geeks')
print(tup1)
n=5

for i in range(int(n)):
    tup1= (tup1,)
    print(tup1)


print(tuple("Geeks"))

tup1 = ('Geeks',)*3
print(tup1)

tup1 = (1,2,3,4)
tup2 = ("Red","Blue","Green")

tup3 = tup1+tup2
print(tup3)
print(tup3[3:5])