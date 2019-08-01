from collections import Counter

'''

Given a binary matrix, print all unique rows of the given matrix. Order of row printing doesn’t matter.

Examples:

Input:
    mat = [[0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0]]
Output:
          (1, 1, 1, 0, 0)
          (0, 1, 0, 0, 1)
          (1, 0, 1, 1, 0)

'''


mat = [[0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0]]

for res in mat:
    if mat.count(res) > 1:
        mat.remove(res)

print(mat)

print()
'''
Solution by using Set as Set contains only Uniq Value
'''

mat = [[0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0]]

mat1 = [[0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0]]

mat = map(tuple,mat)
mat1 = map(tuple,mat1)

#for item in mat:
 #   print (item)

result = set(mat)

print("After filter Duplicate rows")
for item in tuple(result):
    print(item)


#result = set(mat1)
freqDict = Counter(mat1)

print("Solution using Counter")

for row,freq in freqDict.items():
    print(row)


str1 = "geeksforgeeks"
#str1 = map(tuple,str1)
freqDict = Counter(str1)
for (row,freq) in freqDict.items():
    if freq > 1:
        print (row,end=" ")

