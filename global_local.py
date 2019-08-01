import re

x = re.search(r"cat","cat and rat cant be friends")

if "cat" in "cat and rat cant be friends":
    print("Cat is there ")

print(x)
def f():
    global s
    print(s)
    s = "I am  inside the function"
    print(s)


s = "Python is Great"
print(s)
f()
