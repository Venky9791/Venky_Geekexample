fruit = {"orange": "Sour is sour",
          "Apple": "Cider is Cider",
          "Lemon":"Sweet is Swet",
          "Pear": "Hot is Hot"}
swap_fruit = {}

print (fruit)
for f in sorted(fruit.keys()):
    print ("{} is {}".format(f,fruit[f]))
    value = fruit[f]
    swap_fruit[value] = f

print(swap_fruit)
