import re

test_string = "There are 2 apples for 4 persons"

res2 = [int(i) for i in test_string.split() if i.isdigit()]
print (test_string.split())

print("Extract Numebers from rest2 is {0}".format(res2))
#print("Extract String from rest2 is {0}".format(res3))

#test_string = input("Enter the String")
print ("The Orginal String is " + test_string)

res = re.sub("\D","",test_string)
res1 = re.sub("\S","",test_string)
print("The Numbers in the String {0} is {1}".format(test_string,res))

print("The String in the String {0} is {1}".format(test_string,res1))