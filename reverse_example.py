s = "Venky"
print(s)
print (s[::-1])
print(''.join(reversed(s)))
print(len(s) // 2)
#def reverse_string(s):
    #chars = list(s)

def reverse_string3(s):
    """Return a reversed copy of `s`"""
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        print ("value of tmp" + tmp)
        chars[i] = chars[len(s) - i - 1]
        print("Value of char[2] " + chars[i])
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)


print(reverse_string3("Venky"))





