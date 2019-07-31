
#Given a list, print the number of numbers in the given range.

#input=[10,20,30,40,50,60,70] Range : 40-80
#output [40,50,60,70] - 4

input=[10,20,30,40,50,60,70]
#Range : 40-80

l=40
r=80

for i in input:
    if i in range(l,r):
        print (i,end=" ")

print(list(x for x in input if l <= x <= r))
#if 5 in range(1,7):
 #   print("I am in range")
