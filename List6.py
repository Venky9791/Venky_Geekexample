'''

Given a list, print all the sublists of a list.

Examples:

Input  : list = [1, 2, 3]
Output : [[], [1], [1, 2], [1, 2, 3], [2],
         [2, 3], [3]]

Input : [1, 2, 3, 4]
Output : [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4],
         [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
'''

Input = [1, 2, 3]

c=1
new_list=[]
for k in range(0,len(Input)+1):
    if k == 0:
        new_list.append([])
    else:
        for i in range(k,len(Input)+1):
            res = []
            for j in range(c,i+1):
                res.append(j)
            new_list.append(res)
        c+=1




print(new_list)
