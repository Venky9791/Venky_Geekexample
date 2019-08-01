cities = ["Adelaide","Paris","Chennai","Delhi","Newyork"]

# with open ("cities.txt",'w') as city_file:
#     for city in cities:
#         print (city,file=city_file)

cities=[]
with open ("cities.txt",'r') as city_file:
    for city in city_file:
        cities.append(city)
       # print (city,end='')

for city in cities:
    print(city,end='')


