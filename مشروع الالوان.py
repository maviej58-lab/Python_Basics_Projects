colors=[  ]
first=input("Add the first color you like:")
colors.append(first)
user=input("Do you want to add more colors?yes, or no?").lower( )
if user=="yes":
    another=input("Add another color to the list :")
    colors.append(another)
    print("the colors you like are:")
    print(colors)
elif user=="no" :
    print("the color you like is :")  
    print(colors) 
else :
    print("please follow the rules!")    