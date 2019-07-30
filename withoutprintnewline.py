def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multi(n1,n2):
    return n1*n2

def dive(n1,n2):
    return n1 // n2

print("""
1.Addition
2.Subtraction
3.Multiplication
4.Divison
5.Quit
""")

n1 =  int(input("Enter Number one"))
n2 =  int(input("Enter Number two"))
select = input("Select Operations 1,2,3,4,5")





if select == '1':
    print(add(n1,n2))
elif select == '2':
    print(subtract(n1, n2))
elif select == '3':
    print(multi(n1, n2))
elif select == '4':
    print(dive(n1,n2))
