# age = int (input ("Enter your age"))
#
# if ( 18 < age < 30):
#      print (" you are Old enough to go for Holiday")
# elif ( age > 30 and age < 65):
#      print ("Enjoy yor Free time")
# else:
#         print ("You are too young to go for Holiday")
#
# for i in range (1,20):
#     print ("{0:<2} square is {1:<4} Cube is {2:<6}".format(i,i**2,i**3))


for i in range (1,13):
    for j in range (1,13):
        print ("{0} times {1} is {2}".format(j,i,i*j))
    print ("******************")

for state in ["Venky","Deeepak","Vara","Andy"]:
    print ("the State is {}".format(state))

design = "***********"

newchar = ""
for char in range (1,len(design)):
    for j in range (1,char):
         newchar = newchar + design[j]
    print (newchar)


