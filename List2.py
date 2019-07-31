#Given an array, reverse every sub-array formed by consecutive k elements.
#Examples:
#Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#k = 3
#Output:  [3, 2, 1, 6, 5, 4, 9, 8, 7]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original List \n" +  str(arr))
k = 3
new_list = []
c=0
while c <len(arr)+1:
     #new_list.extend(arr[c:c+k][::-1]) 'this is another solution line as well. '
     new_list = new_list + list(reversed(arr[c:c+k]))
     c=c+k
print("After change \n" +  str(new_list))

#print(arr[3:6][::-1])
#print(arr[6:9][::-1])

#print(arr[::-1])
#print(arr[::-1][0:3])
#for i in arr:

 #   print (i)
#sliced_list=arr[::-3]
#print(sliced_list)