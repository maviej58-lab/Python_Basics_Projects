basket=[ ]
fruits=["Apples", "Bananas"]
drinks=["Milk", "Water"]
print(basket)
input("press enter to change the content")
basket.append(fruits)
basket.append(drinks)
basket.append([1, 2, 3])
fruits.insert(0,"Oranges")
fruits.insert(3,"Kiwis")
drinks.insert(0,"Coffee")
drinks.remove("Water")
drinks.insert(2,"Tea")
print("Here is the updated basket")
print(basket)