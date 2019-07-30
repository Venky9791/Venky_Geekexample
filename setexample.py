x = set(["Apple","Orange","Banana","Apple","Orange","Banana"])

y = {"Red","blue","White","Red","blue","White"}
z = {"Red","Green","Yellow","White"}
print(x)
print(y)

print(z.difference(y))
x.add("Mango")
print(x)
print(y.intersection(z))