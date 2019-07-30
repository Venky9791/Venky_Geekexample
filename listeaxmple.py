fruits = ['apple','orange','banana']

mylist = fruits.copy()

print(fruits)

mylist = fruits
mylist.append("Strawberry")
print(fruits)
print(mylist)

fruits.remove("Strawberry")

print(mylist)

mylist.insert(2,"blackcurrent")

print(fruits)

if "banana" in mylist:
    print("Yes {} is present in the List".format("Banana"))

for x in mylist:
    print(x,end=" ",sep="@")

anothercopy = list(mylist)
print(anothercopy)
anothercopy.extend(["Venky","Ryan","Moshin"])
print(anothercopy)
name = [["Venkatesan"],[1,2,3,5]]
name.append((7,8,"Venky"))
print(name[2][2])
if "Venky" in name:
    print("Yes Venky is there ")

print(mylist[:-1])

List = [1,2,3,4,5,6,7,8,9,10]
#List.remove(5)
print(List[::-3])
print(List[5:])
print(List[:-6])
test_list = [1, 3, 5, 5, 4, 5]
print("The test List",str(test_list))


res = (sum(1 for i in test_list if i == 5) >= 3)

if res == 1:
    print("5 Occurs 3 times times  in the List")
else:
    print("5 is NOT Occurs 3 times times  in the List")


def check_numbers(a,b):
    a_set = set(a)
    b_set = set(b)
    if (len(a_set.intersection(b_set))) > 0:
   # if (a_set&b_set):
        print("Element is there in the list")
    else:
        print("Element is not therein the list")

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
check_numbers(a,b)
