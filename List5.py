import re

'''Given a string consisting of alphabets and others characters, remove all the characters other than alphabets and print the string so formed.
Examples:

Input : str = "$Gee*k;s..fo, r'Ge^eks?"
Output : GeeksforGeeks

'''

str = "$Gee*k;s..fo, r'Ge^eks?"

# for char in str:
#     #print (char)
#     if ord(char) in range(ord('a'),ord('z')+1) or  ord(char) in range(ord('A'),ord('Z')+1):
#         print (char , end='')

sep_chars = [char for char in str if ord(char) in range(ord('a'),ord('z')+1) or ord(char) in range(ord('A'), ord('Z')+1)]
#print(sep_chars)
sep_chars = ''.join(sep_chars)
print ("Strip out the strings using ORD function")
print(sep_chars)
print ()
print ("Strip out the strings using Is alph function using for loop")


for i in range(0,len(str)):
    char = str[i]
    if char.isalpha():
        print(char,end='')
print ()
print ("Strip out the strings using List comprehension function ")
sep_chars = [str[i] for i in range(0,len(str)) if str[i].isalpha() ]
sep_chars = ''.join(sep_chars)
print(sep_chars)
print ()
#print(sep_chars)
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
print(email[:m.start()])
print(email[m.end():])
print(email[:m.start()] + email[m.end():])


Input = [0,1,2,3,4,5,6,7,8,9,10]
even = [x for x in Input if x % 2 == 0]
print(even)


'''
You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array.

Examples:
Input  :  arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output :  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 
'''


arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
newarr = []

for i in range (0,2):
    for j in arr:
        if i == 0 and j == 0:
            newarr.append(0)
        elif i == 1 and j == 1:
            newarr.append(1)
print(newarr)


res = [x for x in arr if x == 0] + [x for x in arr if x == 1]
print(res)


arr = [4,2,1,6,9,0,3,7,10,8,5]



for j in range(0,len(arr)-1):
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
            t = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = t

print("Original Arrary arr = [4,2,1,6,9,0,3,7,10,8,5]")
print (arr)

'''
Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts.
1) All elements smaller than lowVal come first.
2) All elements in range lowVal to highVal come next.
3) All elements greater than highVal appear in the end.
The individual elements of three sets can appear in any order.

Examples:

Input: arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]  
        lowVal = 14, highVal = 20
Output: arr = [1, 5, 4, 2, 3, 1, 14, 20, 20, 54, 87, 98, 32]
'''
arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
lowVal = 14
highVal = 20


res = [x for x in arr if x < lowVal] + [x for x in arr if x >= lowVal and x <= highVal] + [x for x in arr if x > highVal]
print(arr)
print (res)

'''
We are given an array of n distinct numbers, the task is to sort all even-placed numbers in increasing and odd-place numbers in decreasing order. The modified array should contain all sorted even-placed numbers followed by reverse sorted odd-placed numbers.
Note that the first element is considered as even because of its index 0
Input:  arr[] = {0, 1, 2, 3, 4, 5, 6, 7}
Output: arr[] = {0, 2, 4, 6, 7, 5, 3, 1}
Even-place elements : 0, 2, 4, 6
Odd-place elements : 1, 3, 5, 7
Even-place elements in increasing order : 
0, 2, 4, 6
Odd-Place elements in decreasing order : 
7, 5, 3, 1
'''

arr =  [0, 1, 2, 3, 4, 5, 6, 7]
even = [x for x in arr if x % 2 == 0 ]
odd =  [x for x in arr if x % 2 != 0]
even = sorted(even) + sorted(odd,reverse=True)
odd = sorted(odd,reverse=True)
print(even)

'Other Solution using List in comprehension'

even = sorted([x for x in arr if x % 2 == 0 ]) + sorted([x for x in arr if x % 2 != 0],reverse=True)
print(even)
#even = sorted(even) + sorted(odd,reverse=True)

matrix = [[0, 1, 1, 1],  [0, 0, 1, 1],  [1, 1, 1, 1],  [0, 0, 0, 0]]
result = list(map(sum,matrix))
print(result.index(max(result)))













