from collections import Counter

'''
Given a binary matrix whose elements are only 0 and 1, we need to print the rows which are duplicate of rows which are already present in the matrix.

Examples:

Input : [[1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [1, 0, 1, 1, 0, 0],
         [1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 1]]

Output : (1, 1, 0, 1, 0, 1)
         (0, 0, 1, 0, 0, 1)

'''

Input = [[1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [1, 0, 1, 1, 0, 0],
         [1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 1]]

for res in Input:
    if Input.count(res) > 1 :
        #print (res)
        pass

sep_list = [res for res in Input if Input.count(res) > 1]
result = map(tuple,sep_list)
result = set(result)
for item in result:
    print(item)


'''
Solution by using Collections Counter method

'''

print("Solution by using @Counter")

Input = [[1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [1, 0, 1, 1, 0, 0],
         [1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 1]]

res = map(tuple,Input)
freqDict = Counter(res)

#print(freqDict)

for (row,freq) in freqDict.items():
    if freq > 1:
        print (row)