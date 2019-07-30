def reverse(seq):
    SeqType = type(seq)
#    print(SeqType)
    emptySeq = SeqType()

 #   print(emptySeq)

    if seq == emptySeq:
        return emptySeq

    restrev = reverse(seq[1:])
    print(restrev)
    first = seq[0:1]
    print(first)
    result = restrev + first
    return result

n = [1,2,3,4,5]
print(n[1:])
print(n[0:1])


def shout(text):
    return text.upper()

print(shout("Hello"))

y = shout
print(y("Hello"))
#print(reverse([1,2,3,4]))

name="Venky"
l = list(name)
print(l)
l.reverse()
print(l)
#print(reverse("HELLO"))