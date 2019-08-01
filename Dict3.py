'''
Given a string and a number N, we need to mirror the characters from N-th position up to the length of the string in the alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.

Examples:

Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.

Input : N = 6
        pneumonia
Output : pnefnlmrz

'''

orginal = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
reverse = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
dict2 =  dict(zip(orginal,reverse))

#pneumonia
input = 'VENKATESAN'
k=5

prefix = input[0:k-1]
suffix = input[k-1:]
mirror=''
#print(prefix)
#print (suffix)


for i in suffix:
 for key,value in dict2.items():
     if i == key:
        mirror = ''.join(mirror) + dict2[key]

print(prefix+mirror)

prefix = input[0:k-1]
suffix = input[k-1:]
mirror=''


for i in suffix:
    mirror = ''.join(mirror) + reverse[orginal.index(i)]

print (prefix+mirror)