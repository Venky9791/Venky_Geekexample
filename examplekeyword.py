import keyword

def find_keyword():
    while (True):
        word = input("Enter a Keyword")
        if word == "Quit":
            break
        else:
            if keyword.iskeyword(word):
                print("You Enterred Python Keyword")
            else:
                print("Its not a Keyowrd")



def myfunc(a,b):
    print(a*b)


if __name__=='__main__':
    a = 1 if 20 > 10 else 0
    myfunc(a,10)


count = 0
while (count<3):
     print("Venky")
     count+=1
else:
    print("In While block")


