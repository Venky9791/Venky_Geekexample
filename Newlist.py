fruits = ["Orange","apple","Pear","Lemon","Kiwi","Strawberry","Orange","apple","Pear","Lemon","Kiwi","Strawberry"]
#print(fruits.index("apple",4))

reverse_fruit = fruits
#print(reversed(fruits))
fruits.append("Pineapple")
print(reverse_fruit)
print(fruits.pop())
print(fruits.pop())
#print(reverse_fruit.sort())

a =12
b=4
print (a+b)
print(a.__add__(b))
print (a.__mod__(b))


list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
l = 40
r = 80

filterlist = list(x for x in list1 if l >=x <=r)
print(filterlist)
print (len(list(x for x in list1 if l >=x <=r)))

my_list = []
start,end = 10,20

if start < end:
    my_list.extend(range(start,end))
    my_list.append(end)
    print(my_list)




