from operator import itemgetter

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]


print("Sorted by Age")
print(sorted(lis,key=itemgetter('age')))

print('\r')
print('\r')
print("Sorted by name")
print(sorted(lis,key=itemgetter('name'),reverse=True))

def myfun(x=5,y=20*5):
    print("X is ",x)
    print("Y is ",y)

myfun(30)

list = ['a', 'b', 'c', 'd', 'e']
print(list[:1])
print(list[10:])

for i in range(5,10,2):
    print(i)


def fn(*argslist):
    for arg in argslist:
        print(arg,end=" ")


def func(**kwargs):
    for name,age in kwargs.items():
        print("%s Age is %s" %(name,age))

func(John=25,Venky=18,Ryan=30)

fn('I am','Geek','Programmer')


def multipls_number(num):
    def product(number):
        return number*num
    return product

num2 = multipls_number(2)
print(num2(2))
print(num2(5))
num6 = multipls_number(1)
print(num6(1))

site_stats = {'site': 'tecbeamers.com', 'traffic': 10000, "type": "organic"}

for k,v in site_stats.items():
    print(k)
    print(v)


no_of_days = 366
leap_year="Yes" if no_of_days == 366 else "No"
print(leap_year)

alist = ["Mango","Apple","Orange"]
astr = "Banana"


alist_obj = enumerate(alist)
astr_obj = enumerate(astr)
print(list(enumerate(alist)) )
