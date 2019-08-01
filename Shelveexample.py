import shelve

with shelve.open ("shelve") as fruit:
     # fruit['Orange'] = "A sweet and sour Fruit"
     # fruit['Apple'] =  "Eat Apple a Day"
     # fruit['Banana'] = "Good for Digestion"
     # fruit['Mango'] = "India's National Fruit"
     # fruit['Pear'] =  "Contains lots of vitamins"


    for key in fruit:
        print (key)
    # while True:
    #     snack = input("Enter a Fruit name")
    #     if snack == "quit":
    #          print("Thankyour for Playing this Game")
    #          break
    #     if snack in fruit:
    #         print ("Thanks for your buying this Fruit"+ snack + "Is" + fruit[snack])
    #     else:
    #         print ("Sorry we dont have this fruit"+  snack)

    ordered_key = list(fruit.keys())
    ordered_key.sort()

    #for key in fruit.value():
     #   print (key)
    #print (fruit.values())

    for f in fruit.items():
         print (f)

    fruit.close()


    #for snack in fruit:
     #    print (snack + "is " + fruit[snack])

