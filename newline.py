a = [1,2,3,4,5]

for i in a:
    print(i ,end=",")

ini_str = 'Geeks\nFor\nGeeks\n'

print("Initial String" + ini_str)

res_str = ini_str.splitlines()
res_str1 = ini_str.rstrip().split("\n")
print("Result String" + str(res_str))
print("Result String" + str(res_str1))

print ("C\\Venky\\Prython")
print("I ' m a 'Geek'")

print ("'I\' a \"Geek\"")

str1 = "|{:<10}|{:^20}|{:>10}|".format('Left','Center','Right')
print(str1)