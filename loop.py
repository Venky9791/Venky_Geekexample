

def emi_calculator(p,r,t):
    r = r / (12*100)
    t = t * 12
    emi = (p*r*pow(1+r,t) / (pow(1+r,t))-1)
    return emi


print("Geeks",end=" ")
print("For Geeks")
a = [1,2,3,4]
for i in range(0,len(a)):
    print(a[i],sep='@')
principal = 34500
rate = 4.5
time = 13
emi = emi_calculator(principal,rate,time)
print("The EMI is " ,emi)


x,y = input("Enter two values ").split('')
print("Numnber of X" , x)
print("Number of Y",y)

x = list(map(int,input("Enter Multiple values").split()))
print("List of Students" , x)

x,y = [int(x) for x in input("Enter two Values").split()]
print("First Number is {} and Second Number is {}".format(x,y))


