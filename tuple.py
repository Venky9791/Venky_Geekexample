x = (0,)

x = (0,1)*2

x = (0,1,2) + (3,4,"Venky")


for item in x:
    print (item,end=' ')

print (x)

'''
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

mat = [      [0, 1, 0, 0, 1],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0]]
tup = ()

res=[]
dup = []
for x in range(0,len(mat)):
    if mat.count(mat[x])==1:
      res.append(mat[x])
    elif mat.count(mat[x])== 2:
      dup.append(mat[x])
print(res)

   # for j in mat:
    #   if mat[x] == j:
     #       print(mat[x])
      #      break
        #print(str(mat[x]),str(mat[j]))

        # else:
        #print(mat[x])
#print(mat[0] == mat[2])
