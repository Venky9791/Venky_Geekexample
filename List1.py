List = []
print("Blank List")
print(List)

List = ['GeeksforGeeks']
print("Printing Single Element" + str(List))


List = ["Banglore","Chennai","Befast"]
print("Printing Different Elements of List   "  + str(List[0]),str (List[1]))
List = [1,2,3,"Belfast","Dublin",1,2,3]
print ("Printing Different values and duplicate values \n" + str(List))

List = [[1,2,3],[4,5,6,7],[8,9,10]]
print ("List inside List \n" + str(List))

List.append("Venky")
List.insert([2][0],"Belfast")
print("After Adding and Inserting \n" + str(List))

List2 = ["English","Tamil","Telugu"]
List.extend(List2)



print("After Extending \n" + str(List))

print("Max of List \n" + str(max([10,30,40,70,80])))