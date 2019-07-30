import itertools

from collections import Counter

print ("Code" *5 + ' ' + "Mantra" *5)

a=5
b=7
a,b=b,a
print("A {0} and B {1}".format(a,b))


mat = [[1,2,3,4],[5,6,7,8]]
print(list(zip(*mat)))

def is_anagram(str1,str2):
    if Counter(str1)== Counter(str2):
        print("The Word is Anagram")
    else:
        print("The word is not Anagram")

is_anagram('abcd','abcd')

A = [[1, 2], [3, 4], [5, 6]]

print(list(itertools.chain.from_iterable(A)))

cities = ["Banglore","Chennai","Delhi"]

for city in cities:
    print(city)
print("\r")

str1 = "Iteration is Easy"

for char in str1:
    print(char,end="")

print('\r')
iterator_obj = iter(cities)
print(iterator_obj.__next__())
print(iterator_obj.__next__())
print(iterator_obj.__next__())



def myFunc(a=10,b=10):

    print("A {0} and B {1}".format(a,b))

xx=10
yy=20
myFunc(xx,yy)

