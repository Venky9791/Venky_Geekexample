''' Given a range of sorted list of integers with some integers missing in between,
write a Python program to find all the missing integers.
Input : [1, 2, 4, 6, 7, 9, 10]
Output : [3, 5, 8]

Input : [5, 6, 10, 11, 13]
Output : [7, 8, 9, 12]

'''

Input = [1, 2, 4, 6, 7, 9, 10]
Input1 = [5, 6, 10, 11, 13]


for i in range(Input[0],Input[len(Input)-1]):
   # print(i)
    if i not in Input:
        print (i,end =' ')

print()
for i in range(Input1[0],Input1[len(Input1)-1]):
   # print(i)
    if i not in Input1:
        print (i,end =' ')

print('\n')
Input = [[1,2, 3],[4, 5, 6],[7, 8, 9],[10,11,12]]

print('\n')
print([y for x in Input for y in x])

#print(res)
res = [x*x for x in range (0,10)]
print(res)