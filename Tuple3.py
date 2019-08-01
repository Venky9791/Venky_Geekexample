'''

Word Count Program
'''


str1 = "This is example program to count the number of words in this line"

print(str1.count(' '))
#print (str1.count(str1.split(' ')))

'''
A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Examples :

Input : 25525511135
Output : [“255.255.11.135”, “255.255.111.35”]
Explanation: 
These are the only valid possible
IP addresses.

Input : "25505011535"
Output : []
Explanation : 
We cannot generate a valid IP
address with this string. 

'''


# Function checks wheather IP digits
# are valid or not.
def is_valid(ip):
    # Spliting by "."
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True


# Function converts string to IP address
def convert(s):
    sz = len(s)

    # Check for string size
    if sz > 12:
        return []
    snew = s
    l = []


# Generating different combinations.
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                # Check for the validity of combination
                if is_valid(snew):
                    l.append(snew)
                    snew = s
    return l

A = "25525511135"
B = "25505011535"
print(convert(A))
print(convert(B))