from collections import Counter
'''

Given an input string str[], generate two output strings. One of which consists of those character which occurs only once in input string and second which consists of multi-time occurring characters. Output strings must be sorted.

Examples:

Input : str = "geeksforgeeks"
Output : String with characters occurring once:
"for".
String with characters occurring multiple times:
"egks"

'''

str1 = "geeksforgeeks"

freqDict = Counter(str1)
one = ''
two=''

for key,value in freqDict.items():
    if value ==1:
        one = ''.join(one)+ key
    elif value > 1:
         two = ''.join(two) + key

print ("String with characters occurring once:  " + one)
print("String with characters occurring multiple times:  " + two)