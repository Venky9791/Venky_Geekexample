months = {
    1:'January',
    2:'Feb',
    3:'March',
    4:'April',
    5:'May'

}

cust = {
    "Venky":45,
    "Ryan" : 40,
    "Wade": 43,
    "Selva" : 39

}

#for key in cust:
 #   print (key,cust[key])

for key,value in cust.items():
    print(key,value)
cust["Nithya"] = 10
#print(cust)
print(max(cust.values()))




print(months[1])
print(months.get(3))
print(sorted(months,reverse=True))

for key,val in months.items():
    print("{} : {}".format(val,key))

if "January" in months:
    print("Jan is there")

month = months.values()
print(month)
for item in cust.keys():
    print(item,cust[item])