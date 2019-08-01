'''

Maintained repetition only
Input :
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
Output :
[23, 15, 2, 14, 14, 16, 20, 52, 2, 48,
15, 12, 26, 32, 47, 54]

'''

lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]

print([x for x in lst1] + [x for x in lst2])

'''
Maintained repetition and order
Input : 
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
Output :
[2, 2, 12, 14, 14, 15, 15, 16, 20, 23, 
26, 32, 47, 48, 52, 54]
'''

print(sorted([x for x in lst1] + [x for x in lst2]))

'''
Without repetition
Input : 
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
Output :
[32, 2, 12, 14, 15, 16, 48, 47, 20, 52, 54, 23, 26]
'''

print(set([x for x in lst1] + [x for x in lst2]))

'''
Union of three lists
Input : 
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
lst3 = [4, 78, 5, 6, 9, 25, 64, 32, 59]
Output :
[32, 64, 2, 4, 5, 6, 9, 12, 14, 15, 16,48, 47, 78, 20, 52, 54, 23, 25, 26,59]

'''

lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
lst3 = [4, 78, 5, 6, 9, 25, 64, 32, 59]

print("Union of Three Lists")
#print(set(lst3).union(set(lst2).union(set(lst1))))
print(list(set().union(lst1,lst2,lst3)))